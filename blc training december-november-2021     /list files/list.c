#include <stdio.h>
#include <dirent.h>
#include <sys/stat.h>
#include <stdlib.h>

void main()
{
    char *path = ".";   // path to the directory
    struct dirent *dir; // directory entry

    DIR *d = opendir(path); // open the directory
    if (d == NULL)
    {
        perror("opendir");
        exit(1);
    }

    while ((dir = readdir(d)) != NULL) // read the directory
    {
        struct stat st;                                                                                // file status information
        char *file_name = dir->d_name;  // file name
        //malloc() dynamic memory
        char *full_path = malloc(strlen(path) + strlen(file_name) + 2);  // full path
        strcpy(full_path, path);  // copy path
        strcat(full_path, "/");       // append slash
        strcat(full_path, file_name);  // append file name
        stat(full_path, &st);           // get file status
        // if it is a regular file and it is less than 2MB and it is older than 45 minutes
        if (S_ISREG(st.st_mode) && st.st_size < 2 * 1024 * 1024 && st.st_mtime < time(NULL) - 45 * 60) 
        {
            printf("%s\n", file_name);
        }
        free(full_path); // free the memory
    }

    closedir(d);
}