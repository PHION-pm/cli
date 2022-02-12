import phion
from phioncli.metadata import __version__
from phioncli.utils import clearConsole
from loguru import logger


def main():
    print("""    
.______    __    __      ______   .__   __. 
|      \  |  |  |  | (_)/  __  \  |  \ |  | 
|       | |__|__|__|   |  |  |  | |   \|  | 
|   ___/  |________| (_)  |  |  | |    \  | 
|   |     |  |  |  |  _|  `--'  | |     \ | 
| __|     |__|  |__| (_)\______/  |______\| 
    """)
    logger.info(f"CLI Version: {__version__}      Core Version: {phion.__version__}")

    menu_options = {
        'View Available Packages': view_packages,
        'Load .phkf': import_package_process,
        'Create Package': create_package_process,
        'Change Settings': change_settings,
    }
    _key_list = list(menu_options.keys())

    while True:
        print('\n\n========== MAIN MENU ==========')
        for key, value in menu_options.items():
            print(str(_key_list.index(key)) + ': ', key)

        print("\nQ: Exit CLI")
        
        user_sel = input("What would you like to do (default=1): ")

        if user_sel == '':
            user_sel = '1'
        elif user_sel.upper() == 'Q':
                exit_cli()

        clearConsole()

        try:
            logger.info(f"User selected {user_sel} - {_key_list[int(user_sel)]}")
            menu_options[_key_list[int(user_sel)]]()
        except IndexError:
            logger.error("Option not found in the menu, try again.")
 

def view_packages():
    pass

def import_package_process():
    pass

def create_package_process():
    pass

def change_settings():
    pass

def exit_cli():
    exit()

if __name__=='__main__':
    main()