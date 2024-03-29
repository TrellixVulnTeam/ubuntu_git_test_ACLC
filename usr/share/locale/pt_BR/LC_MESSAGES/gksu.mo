��    %      D  5   l      @     A  s   C    �  �   �  �   U  �     k   �  �   7  k   �  N   \  _   �  E   	  &   Q	  '   x	  '   �	  (   �	  �   �	  _   �
  �   )     �     �     �            E   3  ,   y  +   �  %   �     �            +        C  	   [     e     r  �  �     *  r   ,     �  �   �  �   J  �     f   �  �   O  g     X   ~  b   �  O   :  +   �  4   �  1   �  0     �   N  h   @  �   �     n     �     �     �     �  Q   �  1   0  ,   b  &   �     �     �  	   �  3   �       
   4     ?     O                          	      !      $                                       "                               %                                    
                    #               
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

%s <b>Incorrect password... try again.</b> <b>Options to use when changing user</b> <b>Would you like your screen to be "grabbed"
while you enter the password?</b>

This means all applications will be paused to avoid
the eavesdropping of your password by a a malicious
application while you type it. <big><b>Missing options or arguments</b></big>

You need to provide --description or --message. <big><b>Unable to determine the program to run.</b></big>

The item you selected cannot be open with administrator powers because the correct application cannot be determined. Advanced options As user: GKsu version %s

 Missing command to run. Open as administrator Opens a terminal as the root user, using gksu to ask for the password Opens the file with administrator privileges Option not accepted for --disable-grab: %s
 Option not accepted for --prompt: %s
 Root Terminal Run program Run: Usage: %s [-u <user>] [options] <command>

 User %s does not exist. _Advanced _login shell _preserve environment Project-Id-Version: gksu 2.0.2-2
Report-Msgid-Bugs-To: kov@debian.org
POT-Creation-Date: 2007-05-11 00:59-0300
PO-Revision-Date: 2010-01-29 23:32+0000
Last-Translator: Américo Monteiro <a_monteiro@netcabo.pt>
Language-Team: Portuguese <traduz@debianpt.org>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Generator: Lokalize 1.0
Plural-Forms: nplurals=2; plural=(n != 1);
 
   --debug, -d
    Escreve informação no ecrã que pode ser
    útil para diagnosticar e/ou resolver problemas.
   --description <description|file>, -D <description|file>
    Fornece um nome descritivo para o comando a
    ser usado na mensagem predefinida, tornando-a melhor.
    Você também pode fornecer o caminho absoluto para um
    ficheiro .desktop. Neste caso será usada a chave Name.
    
   --disable-grab, -g
    Desactiva o "bloqueio" do teclado, rato,
    e foco feito pelo programa quando pergunta pela
    palavra-passe.
   --login, -l
    Faz disto uma shell de login. Cuidado que isto pode causar
    problemas com o Xauthority magic. Corra xhost
    para permitir ao utilizador destinatário abrir janelas no seu
    display!
   --message <message>, -m <message>
    Substitui a mensagem standard mostrada para pedir a
    palavra-passe para o argumento passado à opção.
    Use isto apenas se --description não for suficiente.
   --preserve-env, -k
    Preserva os ambientes actuais, não define $HOME
    nem $PATH, por exemplo.
   --print-pass, -p
    Pede ao gksu para escrever a palavra-passe no stdout, tal
    como ssh-askpass. Útil para usar em scripts com
    programas que aceitam receber a palavra-passe no
    stdin.
   --prompt, -P
    Pergunta ao utilizador se quer ter o teclado e rato
    capturado antes de o fazer.
   --su-mode, -w
    Faz o GKSu usar su, em vez de usar a predefinição
    da libgksu.
   --sudo-mode, -S
    Faz o GKSu usar sudo em vez de su, como se fosse
    corrido como "gksudo".
   --user <user>, -u <user>
    Chama <command> como o utilizador especificado.
 <b>Falhou ao pedir a palavra-passe.</b>

%s <b>Falhou ao executar %s como utilizador %s.</b>

%s <b>Palavra-passe incorrecta... tente de novo.</b> <b>Opções a usar quando muda de utilizador</b> <b>Deseja que o seu ecrã seja "agarrado"
enquanto insere a palavra-passe?</b>

Isto significa que todas as aplicações serão colocadas em pausa
para evitar a intercepção da sua palavra-passe por um programa
malicioso enquanto a escreve. <big><b>Opções ou argumentos em falta</b></big>

Você precisa de fornecer --description ou --message. <big><b>Incapaz de determinar o programa para executar.</b></big>

O item que seleccionou não pode ser aberto com poderes de administrador porque a aplicação correcta não pode ser determinada. Opções avançadas Como utilizador: GKsu versão %s

 Comando para executar em falta. Abrir como administrador Abre um terminal como o utilizador root, usando o gksu para pedir a palavra-passe Abre o ficheiro com privilégios de administrador Opção não aceite para --disable-grab: %s
 Opção não aceite para --prompt: %s
 Terminal de Root Executar programa Executar: Utilização: %s [-u <user>] [opções] <command>

 O utilizador %s não existe. _Avançado shell de _login _preservar o ambiente 