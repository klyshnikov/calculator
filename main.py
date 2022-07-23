#IndexError, RecursionError, OverflowError

import result

print("It is calculator-interpreter. Enter string:\n")

while True:
    main_str = input().replace(' ', '')
    print(result.result(main_str))


