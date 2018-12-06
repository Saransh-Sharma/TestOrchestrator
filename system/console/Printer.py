import datetime

from system.console import Color


def phase(message):
    padding = " **** **** "
    message=padding+message+padding
    print("\n\n\n" + Color.PURPLE + "[{:%H:%M:%S}]".format(
        datetime.datetime.now()) + " " + Color.PURPLE_UNDERLINE + message + Color.END + "\n\n\n")


def error(tag, message):
    message_assembly = ""

    message_assembly += Color.RED + "[{:%H:%M:%S}] - ".format(datetime.datetime.now())
    if tag != "":
        message_assembly += tag + " "
    message_assembly += message + Color.END

    print(message_assembly)


def step(message):
    padding = " ** ** "
    message=padding+message+padding
    print("\n" + Color.YELLOW + "[{:%H:%M:%S}] ".format(datetime.datetime.now()) + message + Color.END + "\n")


def system_message(tag, message):
    message_assembly = ""

    message_assembly += Color.BLUE + "[{:%H:%M:%S}] - ".format(datetime.datetime.now())
    if tag != "":
        message_assembly += tag + " "
    message_assembly += message + Color.END

    print(message_assembly)


def console_highlighted(tag, message, cmd):
    print(Color.BLUE + "[{:%H:%M:%S}] - ".format(datetime.datetime.now())
          + tag + " " + message + Color.GOLD + cmd + Color.END)


def console(message, end):
    print(Color.DARK_PURPLE + "[{:%H:%M:%S}]   > ".format(datetime.datetime.now()) + message + Color.END, end=end)
