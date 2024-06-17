def get_format_name(fname, lname):
    fullname = f'{fname} {lname}'.title()
    return fullname

def main():
    fullname = get_format_name('natchaporn', 'saithon')
    print(fullname)
    
if __name__=='__main__':
    main()