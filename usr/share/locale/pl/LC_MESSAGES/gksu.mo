��            )   �      �     �  s   �      �     �   �  �   [  k     �   �  k   @  N   �  _   �  E   [  &   �  '   �  '   �  �   	  _   �	  �   P
                *  E   @  ,   �  +   �  %   �       +        ?  i  W     �  �   �  @  I  �   �  �     �   
  {   �  �   P  p   (  n   �  x     `   �  +   �  8     /   G  �   w  ]   N  �   �     o  )   �     �  I   �  +     +   ;  %   g     �  4   �     �                                                                                                           
      	                         
   --debug, -d
    Print information on the screen that might be
    useful for diagnosing and/or solving problems.
   --description <description|file>, -D <description|file>
    Provide a descriptive name for the command to
    be used in the default message, making it nicer.
    You can also provide the absolute path for a
    .desktop file. The Name key for will be used in
    this case.
   --disable-grab, -g
    Disable the "locking" of the keyboard, mouse,
    and focus done by the program when asking for
    password.
   --login, -l
    Make this a login shell. Beware this may cause
    problems with the Xauthority magic. Run xhost
    to allow the target user to open windows on your
    display!
   --message <message>, -m <message>
    Replace the standard message shown to ask for
    password for the argument passed to the option.
    Only use this if --description does not suffice.
   --preserve-env, -k
    Preserve the current environments, does not set $HOME
    nor $PATH, for example.
   --print-pass, -p
    Ask gksu to print the password to stdout, just
    like ssh-askpass. Useful to use in scripts with
    programs that accept receiving the password on
    stdin.
   --prompt, -P
    Ask the user if they want to have their keyboard
    and mouse grabbed before doing so.
   --su-mode, -w
    Make GKSu use su, instead of using libgksu's
    default.
   --sudo-mode, -S
    Make GKSu use sudo instead of su, as if it had been
    run as "gksudo".
   --user <user>, -u <user>
    Call <command> as the specified user.
 <b>Failed to request password.</b>

%s <b>Failed to run %s as user %s.</b>

%s <b>Incorrect password... try again.</b> <b>Would you like your screen to be "grabbed"
while you enter the password?</b>

This means all applications will be paused to avoid
the eavesdropping of your password by a a malicious
application while you type it. <big><b>Missing options or arguments</b></big>

You need to provide --description or --message. <big><b>Unable to determine the program to run.</b></big>

The item you selected cannot be open with administrator powers because the correct application cannot be determined. GKsu version %s

 Missing command to run. Open as administrator Opens a terminal as the root user, using gksu to ask for the password Opens the file with administrator privileges Option not accepted for --disable-grab: %s
 Option not accepted for --prompt: %s
 Root Terminal Usage: %s [-u <user>] [options] <command>

 User %s does not exist. Project-Id-Version: gksu 1.9.3
Report-Msgid-Bugs-To: kov@debian.org
POT-Creation-Date: 2007-05-11 00:59-0300
PO-Revision-Date: 2006-08-14 02:03+0200
Last-Translator: Wiktor Wandachowicz <siryes@gmail.com>
Language-Team: Polish <translation-team-pl@lists.sourceforge.net>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
 
   --debug, -d
    Wyświetlanie na ekranie informacji, które mogą być
    przydatne przy diagnozowaniu/rozwiązywaniu problemów.
   --description <opis|plik>, -D <opis|plik>
    Użycie opisowej nazwy w treści komunikatu wyświetlanego
    przed uruchomieniem polecenia, dzięki czemu jest on
    przyjemniejszy. Możliwe jest również podanie pełnej
    ścieżki do pliku .desktop, w tym przypadku będzie użyty
    klucz Name z takiego pliku.
   --disable-grab, -g
    Wyłączenie "przechwytywania" klawiatury, myszy,
    oraz skupienia przez program przy pytaniu o hasło.
   --login, -l
    Uruchomienie w roli powłoki startowej (login shell). Może
    to sprawić problemy z mechanizmami Xauthority. Wskazane
    jest uruchomienie xhost aby umożliwić docelowemu
    użytkownikowi na otwieranie okien na twoim ekranie!
   --message <komunikat>, -m <komunikat>
    Zamiana standardowego komunikatu zapytania o hasło
    na wskazany w tej opcji. Należy używać tylko gdy
    opcja --description nie jest wystarczająca.
   --preserve-env, -k
    Zachowanie bieżących zmiennych środowiska, przykładowo
    nie są zmieniane $HOME ani $PATH.
     Wyświetlanie hasła na standardowym wyjściu (stdout),
    podobnie do ssh-askpass. Przydatne w skryptach
    wykorzystujących programy, które akceptują hasła
    podawane na standardowym wejściu (stdin).
   --prompt, -P
    Zapytanie użytkownika, czy należy przechwycić klawiaturę
    oraz mysz przed wykonaniem.
   --su-mode, -w
    Wymuszenie użycia su przez GKSu, zamiast polegania
    na domyślnym zachowaniu libgksu.
   --sudo-mode, -S
    Wymuszenie użycia sudo przez GKSu zamiast su, podobnie
    jak przy uruchamianiu przez "gksudo".
   --user <użytkownik>, -u <użytkownik>
    Wykonanie <polecenia> przez podanego użytkownika.
 <b>Nie udało się wczytać hasła.</b>

%s <b>Nie można uruchomić %s jako użytkownik %s.</b>

%s <b>Niewłaściwe hasło, spróbuj ponownie.</b> <b>Czy chcesz, aby "przechwycić" ekran
podczas podawania hasła?</b>

Oznacza to, że wszystkie aplikacje będą wstrzymane aby
zapobiec podsłuchaniu hasła przez złośliwą aplikację
w trakcie jego wpisywania. <big><b>Brakujące opcje lub argumenty</b></big>

Należy podać --description lub --message. <big><b>Nie można określić programu do uruchomienia.</b></big>

Wybrany element nie może zostać otwarty z uprawnieniami administratora ponieważ nie można odnaleźć właściwej aplikacji. GKsu wersja %s

 Należy podać polecenie do uruchomienia. Otwórz jako administrator Uruchamia terminal użytkownika root, używając gksu do wczytania hasła Otwiera plik z uprawnieniami administratora Niewłaściwa opcja dla --disable-grab: %s
 Niewłaściwa opcja dla --prompt: %s
 Terminal użytkownika root Użycie: %s [-u <użytkownik>] [opcje] <polecenie>

 Użytkownik %s nie istnieje. 