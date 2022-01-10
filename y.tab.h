/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    AND = 258,
    ARRAY = 259,
    ELSE = 260,
    FOR = 261,
    GO = 262,
    IF = 263,
    NUMBER = 264,
    OR = 265,
    CIN = 266,
    COUT = 267,
    STRING = 268,
    WHILE = 269,
    XOR = 270,
    ID = 271,
    CONST = 272,
    ATRIB = 273,
    EQ = 274,
    NE = 275,
    LE = 276,
    GE = 277,
    LT = 278,
    GT = 279,
    NOT = 280,
    DOT = 281,
    PLUS = 282,
    MINUS = 283,
    DIV = 284,
    MOD = 285,
    MUL = 286,
    OPEN_CURLY_BRACKET = 287,
    CLOSED_CURLY_BRACKET = 288,
    OPEN_ROUND_BRACKET = 289,
    CLOSED_ROUND_BRACKET = 290,
    OPEN_RIGHT_BRACKET = 291,
    CLOSED_RIGHT_BRACKET = 292,
    READ_OP = 293,
    WRITE_OP = 294,
    COMMA = 295,
    SEMI_COLON = 296,
    COLON = 297,
    SPACE = 298,
    CHAR = 299,
    INT = 300,
    RETURN = 301
  };
#endif
/* Tokens.  */
#define AND 258
#define ARRAY 259
#define ELSE 260
#define FOR 261
#define GO 262
#define IF 263
#define NUMBER 264
#define OR 265
#define CIN 266
#define COUT 267
#define STRING 268
#define WHILE 269
#define XOR 270
#define ID 271
#define CONST 272
#define ATRIB 273
#define EQ 274
#define NE 275
#define LE 276
#define GE 277
#define LT 278
#define GT 279
#define NOT 280
#define DOT 281
#define PLUS 282
#define MINUS 283
#define DIV 284
#define MOD 285
#define MUL 286
#define OPEN_CURLY_BRACKET 287
#define CLOSED_CURLY_BRACKET 288
#define OPEN_ROUND_BRACKET 289
#define CLOSED_ROUND_BRACKET 290
#define OPEN_RIGHT_BRACKET 291
#define CLOSED_RIGHT_BRACKET 292
#define READ_OP 293
#define WRITE_OP 294
#define COMMA 295
#define SEMI_COLON 296
#define COLON 297
#define SPACE 298
#define CHAR 299
#define INT 300
#define RETURN 301

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */