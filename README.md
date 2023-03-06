# public_notes

## 💿 Fresh installations of programming languages
#### 1. Python:
- use `apt-get`
#### 2. JavaScript/TypeScript:
- install NVM (look at official GitHub page for installation)
- install Node (run nvm list-remote to see available versions)
- install TypeScript from Node
#### 3. Rust:
- `bash` command from their homepage
#### 4. Haskell:
- ghcup
#### 5. Java:
- install source JDK
- append to `.bashrc`:
```sh
JAVA_HOME=/usr/lib/jvm/YOUR_JAVA_VERSION
export PATH=$PATH:$JAVA_HOME/bin
export JAVA_HOME
```
- verify it worked by running:
```sh
source .bashrc
java -version
```
- install Apache Maven, link: https://maven.apache.org/download.cgi
- append to `.profile`:
```sh
M2_HOME='<location of bin>'
PATH="$M2_HOME/bin:$PATH"
export PATH
```
- verify with `mvn -version`


## 🚀 PopOS
#### Take interactive screenshot
Keyboard shortcut: `Ctrl+Alt+Shift+R`
#### Remove window titles, and use shortcuts to close
Disable `Show Window Titles` and close windows with shortcut `ctrl+q`
#### Keyboard shortcut customizations
```
- Accessibility:
Turn screen reader on or off: 	Disabled
Turn zoom on or off: 		Disabled
Zoom in: 			Disabled
Zoom out: 			Disabled

- Launchers:
Home folder: 			Super+E
Launch email client: 		Disabled
Settings: 			Super+I

- Navigation:
Move to workspace above: 	Ctrl+Super+K
Move to workspace below: 	Ctrl+Super+J
Switch applications:		Disabled
Switch windows:			Super+Tab
Switch windows directly:	Alt+Tab

- Windows:
Toggle fullscreen mode:		Ctrl+Super+Down
Toggle maximation state: 	Ctrl+Super+Up
View split on left: 		Ctrl+Super+Left
View split on right: 		Ctrl+Super+Right
```

## 🪬 PowerShell
#### Micro editor
1. [Click here for downloading binaries](https://github.com/zyedidia/micro/releases)
2. Put in "Program files"
3. add to PATH

#### Create alias
add the following to `$PROFILE`:
```powershell
Set-Alias -Name m -Value micro
```
#### Prompt on newline
```powershell
function prompt {"PS $($executionContext.SessionState.Path.CurrentLocation)$('>' * ($nestedPromptLevel + 1))`r`n"}
```
#### Conditional prompt
```powershell
function prompt
{
	if ( $? )
	{
		Write-Host "$(get-location)" -foregroundcolor DarkGray
		Write-Host "$Env:username 🙇" -nonewline -foregroundcolor DarkRed
	}
	else
	{
		Write-Host "$(get-location)" -foregroundcolor DarkGray
		Write-Host "$Env:username 🧟" -nonewline -foregroundcolor Cyan
	}
	return ' '
}
```

## 🐧 Linux
#### Zombified prompt (appended to `~/.bashrc`)
```
PROMPT_COMMAND='if [ $? = 0 ]; then PS1="${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\n🙍 "; else PS1="${debian_chroot:+($debian_chroot)}\[\033[31;1m\]\u@\h\[\033[31;1m\]:\[\033[31;1m\]\w\[\033[00m\]\n🧟 "; fi'

# alternatively
function prompt
{
        if ( $? )
        {
                "$([char]27)[1;30m$PWD`n$([char]27)[0m$([char]27)[33m$Env:username 💁$([char]27)[0m "
        }
        else
        {
                "$([char]27)[1;30m$PWD`n$([char]27)[0m$([char]27)[1;36m$Env:username 🧟$([char]27)[0m "
        }
}
```
#### Alias for updating (appended to `~/.bashrc`)
```sh
alias u="sudo apt update && time sudo apt upgrade -y"
```
#### Remove personal folders from Ubuntu:
```sh
# delete folders (let 'Desktop' and 'Downloads' remain)
rmdir Music Templates Public Videos/Screencasts Videos
# update folders
xdg-user-dirs-update
# config file at
.config/user-dirs.dirs
# might have to reboot
```

## 💤 VSCode
#### Keyboard shortcuts:
```json
[
  {
    "key": "ctrl+shift+7",
    "command": "editor.action.commentLine",
    "when": "editorTextFocus && !editorReadonly"
  },
  // Toggle between terminal and editor focus:
  {
    "key": "ctrl+[IntlBackslash]",
    "command": "workbench.action.terminal.focus",
    "when": "terminalIsOpen && !terminalFocus"
  },
  {
    "key": "ctrl+[IntlBackslash]",
    "command": "workbench.action.focusActiveEditorGroup",
    "when": "!editorFocus && editorIsOpen"
  },
  {
    "key": "ctrl+k ctrl+q",
    "command": "-workbench.action.navigateToLastEditLocation"
  },
  {
    "key": "ctrl+[Comma]",
    "command": "editor.action.marker.next",
    "when": "editorFocus"
  },
  {
    "key": "ctrl+shift+t",
    "command": "workbench.view.extension.test"
  },
  {
    "key": "ctrl+[Comma]",
    "command": "-workbench.action.openSettings"
  },
  {
    "key": "ctrl+m",
    "command": "-editor.action.toggleTabFocusMode"
  },
  // Map shift+delete to just delete:
  {
    "key": "shift+delete",
    "command": "editor.action.deleteLines",
    "when": "textInputFocus && !editorReadonly"
  },
  {
    "key": "ctrl+shift+[Comma]",
    "command": "testing.runAll"
  },
  {
    "key": "ctrl+shift+[Comma] a",
    "command": "-testing.runAll"
  },
  {
    "key": "ctrl+shift+[Period]",
    "command": "-breadcrumbs.focus",
    "when": "breadcrumbsPossible"
  },
  {
    "key": "ctrl+shift+[IntlBackslash]",
    "command": "-breadcrumbs.toggleToOn",
    "when": "!config.breadcrumbs.enabled"
  },
  {
    "key": "ctrl+shift+[IntlBackslash]",
    "command": "-breadcrumbs.focusAndSelect",
    "when": "breadcrumbsPossible && breadcrumbsVisible"
  },
  {
    "key": "ctrl+shift+[IntlBackslash]",
    "command": "-editor.action.inPlaceReplace.down",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+shift+[IntlBackslash]",
    "command": "workbench.action.terminal.focusNextPane",
    "when": "terminalFocus && terminalHasBeenCreated || terminalFocus && terminalProcessSupported"
  },
  {
    "key": "ctrl+b",
    "command": "-markdown.extension.editing.toggleBold",
    "when": "editorTextFocus && !editorReadonly && editorLangId == 'markdown'"
  },
  {
    "key": "ctrl+shift+backspace",
    "command": "-search.searchEditor.action.deleteFileResults",
    "when": "inSearchEditor"
  },
  {
    "key": "ctrl+shift+-",
    "command": "-notebook.cell.split",
    "when": "editorTextFocus && inputFocus && notebookEditorFocused"
  },
  {
    "key": "ctrl+shift+-",
    "command": "-workbench.action.navigateForward",
    "when": "canNavigateForward"
  },
  {
    "key": "ctrl+shift+backspace",
    "command": "workbench.action.navigateBackInEditLocations"
  },
  {
    "key": "ctrl+shift+-",
    "command": "workbench.action.navigateForwardInEditLocations"
  },
  {
    "key": "alt+l",
    "command": "-toggleFindInSelection",
    "when": "editorFocus"
  },
  {
    "key": "alt+l",
    "command": "-toggleSearchEditorContextLines",
    "when": "inSearchEditor"
  },
  {
    "key": "alt+p",
    "command": "-toggleSearchPreserveCase",
    "when": "searchViewletFocus"
  },
  {
    "key": "alt+p",
    "command": "-togglePreserveCase",
    "when": "editorFocus"
  },
  {
    "key": "alt+p",
    "command": "-keybindings.editor.toggleSortByPrecedence",
    "when": "inKeybindings"
  },
  {
    "key": "alt+k",
    "command": "-keybindings.editor.recordSearchKeys",
    "when": "inKeybindings && inKeybindingsSearch"
  },
  {
    "key": "ctrl+alt+meta+l",
    "command": "editor.action.transformToLowercase"
  },
  {
    "key": "ctrl+alt+meta+u",
    "command": "editor.action.transformToUppercase"
  },
  {
    "key": "ctrl+shift+[Period]",
    "label": "Run C++ file",
    "type": "shell",
    "when": "resourceExtname == .cpp",
    "command": "workbench.action.terminal.sendSequence",
    "args": {
      "text": "g++ ${fileBasename} -o ${fileBasenameNoExtension}.out && ./${fileBasenameNoExtension}.out\n"
    }
  },
  {
    "key": "ctrl+alt+meta+p",
    "command": "java.view.package.newPackage"
  },
  {
    "key": "ctrl+alt+meta+x",
    "command": "workbench.action.toggleActivityBarVisibility"
  },
  {
    "key": "alt+l",
    "command": "editor.action.insertSnippet",
    "when": "editorTextFocus",
    "args": {
      "snippet": "($1)$0"
    }
  },
  {
    "key": "alt+[BracketLeft]",
    "command": "editor.action.insertSnippet",
    "when": "editorTextFocus",
    "args": {
      "snippet": "[$1]$0"
    }
  },
  {
    "key": "alt+[Semicolon]",
    "command": "editor.action.insertSnippet",
    "when": "editorTextFocus",
    "args": {
      "snippet": "{$1}$0"
    }
  },
  {
    "key": "alt+[BracketRight]",
    "command": "editor.action.insertSnippet",
    "when": "editorTextFocus",
    "args": {
      "snippet": "<$1>$0"
    }
  },
  {
    "key": "ctrl+[IntlBackslash]",
    "command": "-editor.action.inPlaceReplace.up",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+[IntlBackslash]",
    "command": "workbench.action.terminal.new",
    "when": "!terminalIsOpen"
  },
  {
    "key": "ctrl+shift+e",
    "command": "-workbench.action.quickOpenNavigatePreviousInFilePicker",
    "when": "inFilesPicker && inQuickOpen"
  },
  {
    "key": "ctrl+l ctrl+e",
    "command": "-latex-workshop.shortcut.emph",
    "when": "editorTextFocus && !editorReadonly && editorLangId =~ /^latex$|^latex-expl3$|^rsweave$|^jlweave$/"
  },
  {
    "key": "ctrl+e",
    "command": "-workbench.action.quickOpenNavigateNextInFilePicker",
    "when": "inFilesPicker && inQuickOpen"
  },
  {
    "key": "ctrl+l ctrl+u",
    "command": "-latex-workshop.shortcut.underline",
    "when": "editorTextFocus && !editorReadonly && editorLangId =~ /^latex$|^latex-expl3$|^rsweave$|^jlweave$/"
  },
  {
    "key": "ctrl+shift+[Comma] ctrl+e",
    "command": "-testing.debugFailTests"
  },
  {
    "key": "ctrl+shift+[Comma] e",
    "command": "-testing.reRunFailTests"
  },
  {
    "key": "ctrl+shift+e",
    "command": "-workbench.view.explorer",
    "when": "viewContainer.workbench.view.explorer.enabled"
  },
  {
    "key": "ctrl+shift+e",
    "command": "workbench.view.explorer"
  },
]
```
