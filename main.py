import os
import os.path
import sys
import importlib
from data.utils import warn, die, path_fname

def story_names():
    '''returns a list of mad lib template names without the .py extension'''
    stories = []
    for d in os.listdir('templates/'):
        if d[-3:].lower() == '.py':
            stories.append(d[0:-3])
    return stories

def usage():
    '''print command line usage information and exit process'''
    prg = path_fname(sys.argv[0])
    msg  = f'usage: py {prg} <-l|story_name>\n'
    msg +=  '  -l : list all story names\n'
    msg +=  '  story_name : name of mad lib template'
    die(msg)

def main():
    '''entry point of command line program'''
    if len(sys.argv) != 2:
        usage()  # exits w/ err code 1 

    # two valid values of first argument: -l or <story_name>
    arg1 = sys.argv[1]

    # -l : list story names
    if arg1 == '-l':
        for s in story_names():
            print(s)
        return

    # arg not '-l', so it's a story name
    if arg1 in story_names():
        fpath = f'templates/{arg1}.py'
        if not os.path.isfile(fpath):
            die(f'no such template file: {fpath}')
        template = importlib.import_module(f'templates.{arg1}')
        print(template.mad_text)
    else:
        die(f'invalid story name: {arg1}\nUse `-l` option to list story names.')

if __name__ == '__main__':
    main()
