from config.log_colors import LOG_COLORS

def print_commands():
    print(f"""{LOG_COLORS["bold_underlined_purple"]}Lego Brick Sorting Machine!{LOG_COLORS["reset"]}""")
    print(f"* {LOG_COLORS['blue']}start{LOG_COLORS['reset']} - Starts the sorting machine")
    print(f"* {LOG_COLORS['blue']}stop{LOG_COLORS['reset']} - Stops the sorting machine")
    print(f"* {LOG_COLORS['blue']}quit{LOG_COLORS['reset']} - Quits the program")

if __name__ == "__main__":
    print_commands()