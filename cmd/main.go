package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"math/rand"
	"os"
	"strings"
	"time"

	"github.com/marcusolsson/tui-go"
)

var cmdar = strings.Fields("$l $t $m") //lessonsList test

type Lesson struct {
	Title    string `json:"title"`
	SubTitle string `json:"subtitle"`
	textsAr  [][]string
	Texts    []string `json:"texts"`
}

type Lessons struct {
	Lessons []Lesson `json:"lessons"`
}

type status_t struct {
	menuOption  int
	menuMode    bool
	curTitle    string   //holds the title of the current lesson
	curSubTitle string   //holds the subtitle of the current lesson
	curText     []string // holds the current text of the lesson
	idx         int      //index of the current word in the text
}

var lessons Lessons

// mainly helpful pointers to tui stuff.
// most of these are global anyway because of the ui var pretty sure.
// a state struct didn't want to work because of some weird global holding that tui-go does
// .. i think ..

var sidebar *tui.Box
var m *tui.Box
var mBox *tui.Box
var progressBox *tui.Progress
var input *tui.Entry
var inputBox *tui.Box
var view *tui.Box
var root *tui.Box
var err error
var ui tui.UI
var lessonsList *tui.List

// init the status (menu options and texts)
func initStatus() *status_t {
	status := &status_t{
		menuOption:  0,
		menuMode:    true, //start in the menu
		curSubTitle: "",
		curText:     []string{""},
		idx:         0,
	}
	return status
}

// init the view box (everything to the right of the sidebar)
// made up of the mBox, progressBox, and inputBox
func initViewBox() *tui.Box {
	view := tui.NewVBox(mBox, progressBox, inputBox)
	view.SetSizePolicy(tui.Expanding, tui.Expanding)
	return view
}

// generate the title sreen text
func initTitleScreen(status *status_t) *tui.Box {
	m := tui.NewVBox()
	label := "  _    _   ___     \n /_)  / )  )_   / / \n/ /  (_/  (__  (_/  \n"
	instructions := "How to use this program:\n\nThere are two modes: menu mode and input mode.\n\nUse the input mode to take the test and use the menu mode to switch between lessons.\n\nYou can switch between the modes by typing in the input box below.\n\n        $i and $t switch to the input.\n\n        $l and $m switch to the menu.\n\nSelect a lesson on the left to get started!"
	m.Append(initM(label))
	m.Append(initM(instructions))
	return m
}

// init m (box that holds the current lesson's text or menu)
func initM(str string) *tui.Box {
	return tui.NewHBox(
		tui.NewSpacer(),
		tui.NewLabel(str),
		tui.NewSpacer(),
	)
}

// init the menu box (box that wraps menu)
func initMenuBox(m *tui.Box) *tui.Box {
	placeholder := tui.NewHBox()
	mBox := tui.NewVBox(placeholder, m, placeholder)
	mBox.SetBorder(true)
	return mBox
}

// init the m box (box that wraps m)
func initMBox(m *tui.Box, status *status_t) *tui.Box {
	placeholder := tui.NewHBox()
	tNS := tui.NewVBox()
	tNS.Append(initM(status.curTitle))
	tNS.Append(initM(status.curSubTitle))
	mBox := tui.NewVBox(placeholder, tNS, placeholder, m, placeholder)
	mBox.SetBorder(true)
	return mBox
}

// init the sidebar that holds the lesson list box
func initSidebar(status *status_t) *tui.Box {
	lessonsList = initLessonList(status)
	sidebar := tui.NewVBox(lessonsList)
	sidebar.SetBorder(true)
	sidebar.SetTitle("lessonsList")
	return sidebar
}

// init the lesson list box
func initLessonList(status *status_t) *tui.List {
	l := tui.NewList()
	l.SetFocused(true)
	for i := 0; i < len(lessons.Lessons); i++ {
		l.AddItems(lessons.Lessons[i].Title)
	}
	l.SetSelected(status.menuOption)
	return l
}

// init the progress box
func initProgressBox(status *status_t) *tui.Progress {
	//fmt.Println(len(status.curText))
	progressBox := tui.NewProgress(len(status.curText))
	progressBox.SetSizePolicy(tui.Expanding, tui.Maximum)
	return progressBox
}

// init the input (entry type where users type into)
func initInput() *tui.Entry {
	input := tui.NewEntry()
	input.SetFocused(true)
	input.SetSizePolicy(tui.Expanding, tui.Maximum)
	return input
}

// init the input box that wraps the input entry
func initInputBox(input *tui.Entry) *tui.Box {
	inputBox := tui.NewHBox(input)
	inputBox.SetSizePolicy(tui.Expanding, tui.Maximum)
	inputBox.SetTitle("Input")
	inputBox.SetBorder(true)
	return inputBox
}

// update the view (reloads m, mBox, view)
func updateView(status *status_t) {
	m = initM(getCurrText(status))
	mBox = initMBox(m, status)
	view = initViewBox()
	progressBox = initProgressBox(status)
	ui.SetWidget(tui.NewHBox(sidebar, view))
}

// init the lessons list
func initLessons() Lessons {
	var l Lessons
	l = extractLessons()
	// Texts -> textAr
	for i := 0; i < len(l.Lessons); i++ {
		for j := 0; j < len(l.Lessons[i].Texts); j++ {
			scrambledTextAr := scrambleArray(strings.Fields(l.Lessons[i].Texts[j]))
			l.Lessons[i].textsAr = append(l.Lessons[i].textsAr, scrambledTextAr)
		}
	}
	scrambleArray(strings.Fields(l.Lessons[0].Texts[0]))

	// FIXME: only scramble once. needs to scramble every time a lesson is selected.

	return l
}

// scramble the array.
func scrambleArray(ar []string) []string {
	MAX_LESSON_TEXT_LEN := 10
	scrambled := []string{}
	seenIndexes := []int{}

	i := 0
	for {
		if i == MAX_LESSON_TEXT_LEN {
			break
		}

		rand.Seed(time.Now().UnixNano())
		r := rand.Intn(len(ar))
		inAr := false
		for _, x := range seenIndexes {
			if x == r {
				inAr = true
				break
			}
		}
		if inAr == false {
			scrambled = append(scrambled, ar[r])
			seenIndexes = append(seenIndexes, r)
		}
		i++
	}
	return scrambled
}

// pick a random lesson. relys on the global menuOption!
func pickLesson(status *status_t) int {
	rand.Seed(time.Now().UnixNano())
	randLessonidx := rand.Intn(len(lessons.Lessons[status.menuOption].textsAr))
	// randLessonIdx := rand.Intn(1)
	return randLessonidx
}

func getLessonTitle(status *status_t, lessonidk int) string {
	return lessons.Lessons[status.menuOption].Title
}

func getLessonSubTitle(status *status_t, lessonidk int) string {
	return lessons.Lessons[status.menuOption].SubTitle
}

func getLessonText(status *status_t, lessonidx int) []string {
	l := lessons.Lessons[status.menuOption].textsAr[lessonidx]
	l = scrambleArray(l)
	return l
}

func main() {
	status := initStatus()
	// init the lessons
	lessons = initLessons()

	// initialize the UI elements -- order matters here.
	sidebar = initSidebar(status)
	m = initTitleScreen(status)
	mBox = initMenuBox(m)
	progressBox = initProgressBox(status)
	input = initInput()
	inputBox = initInputBox(input)
	view = initViewBox()

	// handle sidebar selection
	lessonsList.OnItemActivated(func(fn *tui.List) {
		handleMenuSelection(status, fn.SelectedItem())
	})

	// handle input stuff
	input.OnChanged(func(e *tui.Entry) {
		handleInput(status, e.Text(), m, input, progressBox)
	})
	input.OnSubmit(func(e *tui.Entry) {
		handleSubmit(status, e.Text(), m, input, progressBox)
	})

	// finish initializing UI
	root = tui.NewHBox(sidebar, view)

	// build the UI
	ui, err = tui.New(root)
	if err != nil {
		log.Fatal(err)
	}
	ui.SetKeybinding("Esc", func() { ui.Quit() })
	if err := ui.Run(); err != nil {
		log.Fatal(err)
	}
}

// when a sidebar lesson is selected
// updates: menuMode, lessonsList, menuOption, idx, curText
func handleMenuSelection(status *status_t, selectedLesson string) {
	selectInput(status) //switch menu mode and deselect
	status.idx = 0
	for i := 0; i < len(lessons.Lessons); i++ {
		if lessons.Lessons[i].Title == selectedLesson {
			status.menuOption = i
		}
	}
	lessonidx := pickLesson(status)
	status.curText = getLessonText(status, lessonidx)
	status.curTitle = getLessonTitle(status, lessonidx)
	status.curSubTitle = getLessonSubTitle(status, lessonidx)
	updateView(status) //reload the view
}

// when the input changes
// checks word on space input and resets when user types something weird
func handleInput(status *status_t, e string, m *tui.Box, input *tui.Entry, p *tui.Progress) {
	// safety
	if len(e) == 0 {
		return
	}
	// check if we are in menuMode, only allow commands
	if status.menuMode == true && e[0:1] != "$" {
		input.SetText("")
		return
	}

	// ignore sidebar selection keywords
	if status.menuMode == true && (e[len(e)-1:] == "j" || e[len(e)-1:] == "k") {
		input.SetText("")
		return
	}

	// spacebar: check word
	if e[len(e)-1:] == " " {
		e = e[:len(e)-1]
		handleInputNormal(status, e, m, input, p)
	}
}

// handle if a cmd was attemped to be submitted (pressed enter)
// runs commands if valid, resets input on invalid command
func handleInputCmd(status *status_t, e string, m *tui.Box, input *tui.Entry, p *tui.Progress) {

	// only allow one-letter commands
	if len(e) != 2 {
		input.SetText("")
		return
	}

	// command switching. alias'd commands are fine!
	switch e[1:2] {
	case "l":
		selectMenu(status)
	case "m":
		selectMenu(status)
	case "t":
		selectInput(status)
	case "i":
		selectInput(status)
	}

}

// selects the sidebar.
// updates menuMode, lessonsList
func selectMenu(status *status_t) {
	status.menuMode = true
	lessonsList.SetFocused(true)
	lessonsList.SetSelected(status.menuOption)
}

// selects the input.
// updates menuMode, lessonsList
func selectInput(status *status_t) {
	status.menuMode = false
	lessonsList.SetFocused(false)
	lessonsList.SetSelected(-1)
}

// checks and handles when the word is correct.
// updates idx, input, progress bar, updates view
func handleInputNormal(status *status_t, e string, m *tui.Box, input *tui.Entry, p *tui.Progress) {
	match := checkWord(status, e)
	if match {
		handleCorrectWord(status, m, input, p)
	} else {
		// don't allow spaces in typos. maybe change in the future.
		input.SetText(e)
	}

	// pressed space after finishing the last word.
	if getCurrText(status) == "" {
		completeLesson(status, m, input, p)
		status.idx = 0
	}
}

// handles when the correct word was submitted!
// updates status.idx, input, progress bar, updates view
func handleCorrectWord(status *status_t, m *tui.Box, input *tui.Entry, p *tui.Progress) {
	status.idx += 1
	input.SetText("")
	updateView(status)
	p.SetCurrent(status.idx)
}

// handle sumbitting (pressing enter) the input
// can update input, idx, progress bar, view, lots of stuff
func handleSubmit(status *status_t, e string, m *tui.Box, input *tui.Entry, p *tui.Progress) {
	// safety
	if len(e) == 0 {
		return
	}

	// if a cmd
	if e[0:1] == "$" {
		handleInputCmd(status, e, m, input, p)
	}

	// enter can complete a lesson, but only if it's the end of the last word.
	if status.idx == len(status.curText)-1 && checkWord(status, e) {
		completeLesson(status, m, input, p)
	} else {
		input.SetText("")
	}
}

// campare the input word to the current word in the text
// returns boolean
func checkWord(status *status_t, e string) bool {
	if e == status.curText[status.idx] {
		return true
	}
	return false
}

// get the text from the current index onward (returns a string)
// used to update the view
func getCurrText(status *status_t) string {
	s := ""
	for i := status.idx; i < len(status.curText); i++ {
		s += status.curText[i] + " "
	}
	return s
}

// notifies the lesson is complete. resets the index
// TODO: updates what?
func completeLesson(status *status_t, m *tui.Box, input *tui.Entry, p *tui.Progress) {
	m.Remove(1)
	m.Append(tui.NewHBox(
		tui.NewLabel("Completed lesson!"),
		tui.NewSpacer(),
	))
	input.SetText("")
	p.SetCurrent(len(status.curText))
	selectMenu(status)
}

// extract the lessons from the lessons config file
func extractLessons() Lessons {
	var l Lessons
	jsonFile, _ := os.Open("lessons.json")
	byteValue, _ := ioutil.ReadAll(jsonFile)
	json.Unmarshal(byteValue, &l)
	jsonFile.Close()
	return l
}
