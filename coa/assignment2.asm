; Assignment 2: Print Shape
.MODEL SMALL
.STACK 100H
.DATA
    star DB '#$'
    newline DB 0DH,0AH,'$'
.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    MOV CX, 5        ; Number of lines
    MOV BL, 1        ; Start with 1 #

PRINT_LINES:
    MOV DL, BL       ; Copy counter
    PUSH CX          ; Save outer loop counter

PRINT_HASHES:
    LEA DX, star
    MOV AH, 9
    INT 21H
    DEC DL
    JNZ PRINT_HASHES

    ; Print newline
    LEA DX, newline
    MOV AH, 9
    INT 21H

    INC BL           ; Increase number of #
    POP CX
    LOOP PRINT_LINES

    MOV AH, 4CH
    INT 21H
MAIN ENDP
END MAIN
