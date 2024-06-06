#ifndef _SHELL_H_
#define _SHELL_H_
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <limits.h>
#include <fcntl.h>
#include <errno.h>
#define READ_BUF_SIZE 1024
#define WRITE_BUF_SIZE 1024
#define BUF_FLUSH -1
#define CMD_NORM	0
#define CMD_OR		1
#define CMD_AND		2
#define CMD_CHAIN	3
#define CONVERT_LOWERCASE	1
#define CONVERT_UNSIGNED	2
#define USE_GETLINE 0
#define USE_STRTOK 0
#define HIST_FILE	".simple_shell_history"
#define HIST_MAX	4096

extern char **environ;


/**
 * struct liststr - singly linked list
 * @num: the number field
 * @str: a string
 * @next: points to the next node
 */
typedef struct liststr
{
	int num;
	char *str;
	struct liststr *next;
} list_t;

/**
 *struct passinfo - contains pseudo-arguements to pass into a function,
 *		allowing uniform prototype for function pointer struct
 *@arg: a string generated from getline containing arguements
 *@argv: an array of strings generated from arg
 *@path: a string path for the current command
 *@argc: the argument count
 *@line_count: the error count
 *@err_num: the error code for exit()s
 *@linecount_flag: if on count this line of input
 *@fname: the program filename
 *@env: linked list local copy of environ
 *@environ: custom modified copy of environ from LL env
 *@history: the history node
 *@alias: the alias node
 *@env_changed: on if environ was changed
 *@status: the return status of the last exec'd command
 *@cmd_buf: address of pointer to cmd_buf, on if chaining
 *@cmd_buf_type: CMD_type ||, &&, ;
 *@readfd: the fd from which to read line input
 *@histcount: the history line number count
 */
typedef struct passinfo
{
	char *arg;
	char **argv;
	char *path;
	int argc;
	unsigned int line_count;
	int err_num;
	int linecount_flag;
	char *fname;
	list_t *env;
	list_t *history;
	list_t *alias;
	char **environ;
	int env_changed;
	int status;

	char **cmd_buf; /* pointer to cmd ; chain buffer, for memory mangement */
	int cmd_buf_type; /* CMD_type ||, &&, ; */
	int readfd;
	int histcount;
} info_t;

#define INFO_INIT \
{NULL, NULL, NULL, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, 0, 0, NULL, \
	0, 0, 0}

/**
 *struct builtin - contains a builtin string and related function
 *@type: the builtin command flag
 *@func: the function
 */
typedef struct builtin
{
	char *type;
	int (*func)(info_t *);
} builtin_table;

int hash(info_t *, char **);
int find_builtin_func(info_t *);
void find_command(info_t *);
void f_cmd(info_t *);
void _eputs(char *);
int _eputchar(char);
char **strtow(char *, char *);
char **strtoww(char *, char);
int _putfd(char c, int fd);
int _putsfd(char *str, int fd);
char *stringcopy(char *, char *);
char *_strdup(const char *);
void _puts(char *);
int stringlen(char *);
int stringcompare(char *, char *);
void *_realloc(void *, unsigned int, unsigned int);
char *startswith(const char *, const char *);
char *stringcat(char *, char *);
char *_strchr(char *, char);
int _putchar(char);
char *strincopy(char *, char *, int);
char *strincat(char *, char *, int);
char *memsetter(char *, char, unsigned int);
void freeyer(char **);
int bitfree(void **);
int is_interactive_func(info_t *);
int is_delimeter(char, char *);
int _isalpha(int);
int _atoi(char *);
int is_command(info_t *, char *);
char *duplicates(char *, int, int);
char *pathfinder(info_t *, char *, char *);
int _erratoi(char *);
void printerror(info_t *, char *);
int print_d(int, int);
char *convert_number(long int, int, int);
int mineownexit(info_t *);
int replace_string(char **, char *);
int mineowncd(info_t *);
int mineownhelp(info_t *);
void remove_comments(char *);
int minehist(info_t *);
ssize_t get_input(info_t *);
void sigintHandler(int);
int minalias(info_t *);
void clear_info(info_t *);
void set_info(info_t *, char **);
int _getline(info_t *, char **, size_t *);
void free_info(info_t *, int);
char *_getenv(info_t *, const char *);
int _myenv(info_t *);
int _mysetenv(info_t *);
int _myunsetenv(info_t *);
int pop_env_list(info_t *);
char **get_environ(info_t *);
int _unsetenv(info_t *, char *);
int _setenv(info_t *, char *, char *);
char *get_hist_file(info_t *info);
int write_hist(info_t *info);
int read_hist(info_t *info);
int build_hist(info_t *info, char *buf, int linecount);
int renumber_history(info_t *info);
list_t *add_node(list_t **, const char *, int);
list_t *add_node_end(list_t **, const char *, int);
size_t print_list_str(const list_t *);
int delete_node_at_index(list_t **, unsigned int);
void free_list(list_t **);
size_t lenlist(const list_t *);
char **list_to_string(list_t *);
size_t print_list(const list_t *);
list_t *node_starts_with(list_t *, char *, char);
int ischain(info_t *, char *, size_t *);
void check_chain(info_t *, char *, size_t *, size_t, size_t);
int replace_alias(info_t *);
int replace_vars(info_t *);
ssize_t get_node_index(list_t *, list_t *);
#endif