/*
 * Scyther : An automatic verifier for security protocols.
 * Copyright (C) 2007-2020 Cas Cremers
 * 
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 */

#ifndef ERROR
#define ERROR

//! usestderr is defined iff we use it
#define USESTDERR

//! Types of exit codes
enum exittypes
{ EXIT_NOATTACK = 0, EXIT_ERROR = 1, EXIT_ATTACK = 3 };

void vprintfstderr (char *fmt, va_list args);
void printfstderr (char *fmt, ...);
void error_die (void);
void error_pre (void);
void error_post (char *fmt, ...);
void error (char *fmt, ...);
void warning_pre (void);
void warning (char *fmt, ...);

#endif
