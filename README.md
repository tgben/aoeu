# Aoeu
## A terminal based Dvorak teaching application for programmers

Built to help programmers who want to switch to Dvorak quickly get up to speed with their new layout.

## Practice what is most important to programmers:
  * common shell commands,
  * common phrases and variables,
  * and more.

![](/img/aoeu-menu.png)

## Lessons built around typing tests for useful practice:

![](/img/aoeu-shell.png)
![](/img/aoeu-language.png)

## Installation and Setup

### Prerequisites
- Go 1.16 or later
- Terminal with color support

### Setup
1. Clone this repository
2. Navigate to the project directory
3. Initialize Go module:
   ```bash
   go mod init github.com/tgben/aoeu
   go mod tidy
   ```

### Running the Application
```bash
# From the project root directory
go run main.go
```

Or build and run:
```bash
go build -o aoeu main.go
./aoeu
```

### Running Tests
```bash
go test -v
```

## Usage

### Controls
- `$l` or `$m`: Switch to menu mode (lesson selection)
- `$i` or `$t`: Switch to input mode (typing practice)
- `Esc`: Quit application
- `Space`: Check word completion during typing
- `Enter`: Submit word or complete lesson

### Lesson Structure
The application loads lessons from `lessons.json`. Each lesson contains:
- **Title**: Displayed in the sidebar
- **Subtitle**: Description shown during practice
- **Texts**: Arrays of practice content that get scrambled for variety
