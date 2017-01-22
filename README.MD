#Vocode - Voice to code assistant 

Vocode is designed to be an assistive voice-to-code program.

## User Stories 

* [x] Create if statements using unique grammars
* [x] Create for loops
* [x] Create while loops
* [x] Move curser directionally
* [x] Scroll page up
* [x] Scroll page down
* [x] Define functions 
* [x] Define variables
* [x] Define dictionaries
* [x] Define arrays 
* [x] Define sets 
* [x] Undo
* [x] Redo
* [x] Select all
* [x] Select line
* [x] Select character
* [x] Delete
* [x] Delete line
* [x] Copy
* [x] Paste
* [ ] Single click install

## Notes
`_vocode.py` is the main file that runs the Vim grammar engine. When making
changes to other files, poke this file to make sure Natlink will detect the
changed files.

## Documentation

Vocode 2017 Official Documentation

MODE CHANGE
----------------------------------------------------------------------------------------------------
Write  mode                        insert
Visual  mode                         escape

EDITING/ACTIONS
----------------------------------------------------------------------------------------------------
Undo                             undo | scratch | whoops
Redo                             redo
Total line redo                        <num> redo
Select all                         select all
Select line                        select line
Select single character                    select char
Delete                            zap word
Delete multiple words                    zap <num> word[s]
Delete line                        strike | delete line
Save                            save
Quit                            quit
Paste                             paste
Paste above                        paste above
Copy                            copy
Copy multiple lines above                 copy <num> line[s] above
Copy multiple lines below                    copy <num> line[s] above
Cut                            cut
Cut multiple lines    above                    cut <num> line[s] above
Cut multiple lines below                     cut <num> line[s] below

*******
Go to line                        gotoline
Find & Replace                        replace <n>
Find a word                        find <n>
*******

NAVIGATION
----------------------------------------------------------------------------------------------------
Change windows -- move to the right             window right
Change windows -- move to the left             window left
Change windows -- move to the down             window down
Change windows -- move to the up             window up
Change tab(s)                         next tab
Move right multiple words                 [go] right <num> word[s]
Move left multiple words                     [go] left <num> word[s]
Go to bottom of page                    bottom
Go to top of page                        top
Up arrow                            up
Down arrow                         down
Left arrow                        left
Right arrow                        right
Scroll page up                        page up
Scroll page down                        page down

CODE
----------------------------------------------------------------------------------------------------
******
variableInCamelCase                    var camel <text>
varible_default                        var default <text>
VariableClass                        var class <text>
If condition                        if <var>
if equals (checks if two inputs are equal)            If equals <varA> <varB>
Else if                            else if <var>
else                             else
For :                            for
For i in range(start, end):                    for [from] <start> to <end>
While :                            while
List                             list
Set                            set
+=                            plus equals
<=                             <numA> less equal <numB>
>=                            <numA> great equal <numB>
>                            <numA> great <numB>
<                             <numA> less <numB>
+                            <varA> plus <varB>
-                                <varA> minus <varB>
/                                <varA> divide <varB>
*                                <varA> (mult|multiply|times) <varB>
%                            <varA> mod[ulus] <varB>
=                            assign to
==                            double equal
[] (array)                             whomp (array | access)
dict()                             whomp (lookup|dictionary)
Set()                             whomp set
                     
*****

Formatting
----------------------------------------------------------------------------------------------------    
Input parenthesis                     parns
Input brackets                        brax
Input curly braces                    curly
Input quotes                        string        

