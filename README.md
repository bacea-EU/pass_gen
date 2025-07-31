# Password Generator
A simple Python command-line password generator that allows you to customize the password length and character set (letters, numbers, special characters).

# Usage
## Options
- len <number>: Set the password length (default: 16)
- n: Include numbers (0-9)
- s: Include special characters (e.g., !@#$%^&)
- l: Include letters (A-Z, a-z)
If no options are provided, the generator defaults to using all character types.

# Examples

Generate a 20-character password with letters and numbers:
```bash
python pass_gen.py -len 20 -l -n
```
Generate a 12-character password with all character types:
```bash
python pass_gen.py -len 12
```
Generate a password with only special characters:
```bash
python pass_gen.py -len 10 -s
```
Output
The generated password will be printed to the console:
```bash
Generated password: a8!Bz2@Qw#1L
```
