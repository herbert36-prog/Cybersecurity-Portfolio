## Personal Reflection

I found this room quite challenging, particularly when working with the different Linux commands and understanding how they worked together. Some commands contained multiple options, variables and symbols, which initially made it difficult to understand what was happening.

For example, I learned commands such as:

- `pwd` – displays the current working directory.
- `cd` – changes the current directory.
- `ls -la` – lists files and folders, including hidden files, in a detailed format.
- `cat` – displays the contents of a file.
- `grep` – searches files for specific words or patterns.
- `chmod +x filename.sh` – gives a script permission to be executed.
- `./filename.sh` – runs a script from the current directory.

The Bash scripting exercises were especially challenging because I struggled to follow the logic behind variables, loops and conditional statements. For example, I initially found a command such as `grep -q "$flag" "$file"` confusing. I learned that `grep` searches for text, `-q` enables quiet mode, `$flag` represents the keyword being searched for, and `$file` represents the file being checked.

The practical exercise helped demonstrate how these concepts could work together. The script searched through log files in the `/var/log` directory to find a specific keyword. By breaking the script into smaller sections, I gained a better understanding of how variables store information, loops process multiple files and `grep` searches for specific text.

Although I found the room difficult, it highlighted an area of Linux that I need to improve. I want to become more comfortable using the terminal, understanding commands and writing basic Bash scripts. These skills are particularly relevant to cybersecurity because Linux commands can be used to investigate system activity and search authentication logs during security investigations.
