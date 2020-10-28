def banner_text(text, width=80):
    if len(text) > width - 4:
        raise ValueError('String "{}" is larger than specified width {}'
                         .format(text, width))
    if text == '*':
        print('*' * width)
    else:
        output_string = '**{}**'.format(text.center(width - 4))
        print(output_string)


# stings to test the function
banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(" ", 80)
banner_text("When you're feeling in the dumps,", 80)
banner_text("Don't be silly chumps,", 66)
banner_text("Just purse your lips and whistle - that's the thing!", 66)
banner_text("And... always look on the bright side of life...", 66)
banner_text("*", 66)
