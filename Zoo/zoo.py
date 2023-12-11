"""Feldman: nice, great"""

print("I Love animals!")
print("Let's check out the animals...")
print("The deer looks fine.")
print("The lion looks healthy.")
camel = r"""
The camel habitat...
 ___.-''''-.
/___ @     |
',,,,.     |          _.'''''''._
     '     |        /            \
     |     \    _.-'              \
     |      '.-'                    '-.
     |                                 ',
     |                                  '',
      ',,-,                             ':;
           ',,| ;,,                   ,' ;;
              ! ; !'',,,',',,,,'!     ;  ;:
            :  ;  ! !       ! ! ;     ;  :;
            ; ;    ! !      ! !  ;    ;  ;,
          ;  ;     ! !     ! !     ;   ;
          ; ;      ! !    ! !        ;   ;
         ;,,        !,!   !,!        ; , ;
         /_I       L_I   L_I         /_ I
Look at that!"""
print(camel)
lion = r"""The lion habitat...
                                                                  ,w.
                                                                ,YWMMw ,M ,
                                        _.---.._   __..---._.'MMMMMw,wMWmW,
                                    _.-""       '''           YP"WMMMMMMMMMb,
                                 .-' __.'                  .'     MMMMW^WMMMM;
                  _,           .'.-'"; `,      /`     .--""      :MMM[==MWMW^;
               ,mM^"        ,-'.'   /   ;     ;      /    ,       MMMMb_wMW" @\
              ,MM:      . .'.-'   .'      ;   `\    ;      `,     MMMMMMMW `"=./`-,
              WMMm__,-'.'        /       _.\    F'''-+,,    ;_,_.dMMMMMMMM[,_ / `=_}
              "^MP__.-'       ,-'  _.--""   `-, ;       \   ; ;MMMMMMMMMMW^``; __|
                           /     .'      ; ;             )  ) `{    \  `"^W^`, \ :
                          /     .'      /  (           .'   /       Ww._    `. `"
                         /     Y,       `, `-,=,_{         ;        MMMP`""-, `-._.-,
                        (--, )            `,_ / `) \/"")             ^"     `-, -;"\:
The lion is roaring!"""
deer = r"""The deer habitat...
              /|       |\
           `__\\       //__'
               ||    ||
             \__`\   |'__/
               `_\\  //_'
               _.,:---;,._
               \_:     :_/
                 |@. .@|
                 |     |
                ,\.-./ \
                ;;`-' `---__________-----.-.
                ;;;                       \_\
                ';;;                       |
                 ;    |                    ;
                  \   \    \         |    /
                   \_, \   /        \    |\
                     |';| |,,,,,,,,/ \   \ \_
                     |  | |           \  /   |
                     \  \ |            | / \ |
                     | || |            | | | |
                     | || |            | | | |
                     |_||_|            |_| |_|
                     /_//_/            /_/ /_/
Pretty good!"""
goose = r"""The goose habitat...

                                         _
                                     ,-"" "".
                                   ,'   ____ `.
                                ,'    ,'    `. `._
     (`.          _..--.._    ,'    ,'        \   \
    (`-.\     .-""         ""'     /          ( d _b
   (`._   `-"" ,._                (            `-( \
  <_   `      ( <`<                \             `-._\
   <`-         (__< <               :
    (__          (_<_<              ;
      `------------------------------------------
Beautiful!"""
bat = r"""The bat habitat...
                _________________             _________________
                   ~-.           \   |\___/|  /            .-~
                       ~-.        \  / o o \ /         .-~
                          >        \ \  W  //         <
                         /           /~---~\         \
                        /_           |      |        _\
                           ~-.       |      |    .-~
                              ;      \      /    i
                            /___     /\    /\   ___\
                                ~-.  / \_ /  \  .-~
                                   V           V
It's doing fine."""
rabbit = r"""The rabbit habitat...
                 ,
                /|     __
               / |  ,-~ /
              Y :|  // /
              | jj /( .^
              >-"~"-v"
             /       Y
            jo  o    |
           ( ~T~     j
            >._-' _./
           /   "~"  |
           Y    _,  |
          /| ;-"~ _ l
         / l/ ,-"~ \
         \//\/   .- \
          Y     /    Y
          l     I    !
          ]\   _\    /"\
         (" ~----( ~ Y. )
It looks fine!"""
animals = [camel, lion, deer, goose, bat, rabbit]
number = int(input("Please enter the number of the habitat you would like to view:"))
print(animals[number])
print("You've reached the end of the program.")
while True:
    number = input("Please enter the number of the habitat you would like to view:")
    if number == "exit":
        print("See you later!")
        break
    print(animals[int(number)])
