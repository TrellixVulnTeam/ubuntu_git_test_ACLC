GOOF----LE-8-2.0ëA      ] q 4     h"      ] g  guile¤	 ¤	g  process-use-modules¤	 ¤	 ¤	g  	aisleriot¤	g  	interface¤	 ¤		 ¤	
g  api¤	
 ¤	 ¤	g  ice-9¤	g  format¤	 ¤	 ¤	g  BASE-VAL¤					 ¤	g  
foundation¤										 ¤	g  tableau¤	g  reserve¤	g  stock¤	g  waste¤	g  initialize-playing-area¤	g  set-ace-low¤	g  make-standard-deck¤	g  shuffle-deck¤	g  add-normal-slot¤	g  DECK¤	g  add-blank-slot¤	 g  add-carriage-return-slot¤	!g  VERTPOS¤	"e  0.2¤	#g  add-extended-slot¤	$g  down¤	%e  0.1¤	&e  0.25¤	'g  deal-cards-face-up¤	(	
 ¤	)g  
deal-cards¤	*	
	
	
	
	
	
	
	
	
	
	
	
										 ¤	+g  flip-top-card¤	,g  add-to-score!¤	-g  	get-value¤	.g  get-top-card¤	/g  give-status-message¤	0g  new-game¤	1g  set-statusbar-message¤	2g  string-append¤	3g  get-stock-no-string¤	4f     ¤	5g  get-reserve-no-string¤	6g  get-base-string¤	7g  get-redeals-string¤	8g  _¤	9f  Stock left:¤	:f   ¤	;g  number->string¤	<g  length¤	=g  	get-cards¤	>f  Reserve left:¤	?f  Base Card: Ace¤	@f  Base Card: Jack¤	Af  Base Card: Queen¤	Bf  Base Card: King¤	Cf   ¤	Df  Base Card: ¤	Ef  Redeals left:¤	Fg  FLIP-COUNTER¤	Gg  member¤	Hg  is-visible?¤	Ig  button-pressed¤	Jg  empty-slot?¤	Kg  fill-tableau-slot¤	Lg  move-n-cards!¤	Mg  complete-transaction¤	Ng  get-suit¤	Og  ace¤	Pg  king¤	Qg  
droppable?¤	Rg  reverse¤	Sg  button-released¤	Tg  
flippable?¤	Ug  	dealable?¤	Vg  
flip-stock¤	Wg  do-deal-next-cards¤	Xg  button-clicked¤	Y	 ¤	Z	 ¤	[	 ¤	\	 ¤	]g  button-double-clicked¤	^g  game-won¤	_g  get-hint¤	`g  	game-over¤	ag  check-a-foundation¤	bg  	hint-move¤	cg  find-empty-slot¤	dg  check-to-foundation¤	eg  check-empty-slot¤	fg  check-to-tableau¤	gg  check-tableau¤	hf  Move waste back to stock¤	if  Deal a card¤	jg  get-options¤	kg  apply-options¤	lg  timeout¤	mg  set-features¤	ng  droppable-feature¤	og  dealable-feature¤	pg  
set-lambda¤C 5 h¸7  y  ] 4	 >  "  G  
RRR	
R
RR !"#$%&'()*+,-./    hÐ  I  ] 4>   "  G  4>   "  G  4>   "  G  4>   "  G  4>  "  G  4>  "  G  4	>   "  G  4
>  "  G  4
>  "  G  4
>  "  G  4
>  "  G  4>   "  G   4>  "  G   4>  "  G   4>  "  G   4>  "  G   4>  "  G   4>  "  G   4>  "  G   4>  "  G   4>  "  G  4
>  "  G  4
>  "  G  4	>  "  G  4	>  "  G  4	>  "  G  4	>  "  G  4		>  "  G  4	>  "  G  4	>  "  G  4	>  "  G  4	>  "  G  4>  "  G  44	55 4>   "  G  			 C  A      g  filenamef  eagle-wing.scm
	
							#			3			C	 		I	 		N	 		W	!		Z	!		\	!		a	!		j	#		z	$		}	$			$	 	$	 	%	 	%	 	%	 	%	  	&	 £	&	 ¥	&	 ª	&	 ³	'	 ¶	'	 ¸	'	 ½	'	 Æ	)	 Ù	*	 Ú	*	 Ü	*	 Ý	+	 à	+	 ä	+	 é	+	 õ	,	 ö	,	 ø	,	 ù	-	 ü	-	 	-		-		.		.		.		/		/		/	!	/	-	0	.	0	0	0	1	1	4	1	8	1	=	1	I	2	J	2	L	2	M	3	P	3	R	3	W	3	c	4	d	4	f	4	g	5	j	5	n	5	s	5		6		6		6		7		7		7		7		8		8		8		9	¢	9	¦	9	«	9	·	:	¸	:	º	:	»	;	¾	;	Â	;	Ç	;	Ð	=	Õ	=	Ú	=	ã	>	è	>	í	>	ö	@		A		B	,	C	>	D	P	E	b	F	t	G		H		J	©	K	¬	K	´	K	¶	K	·	M	Í	O	 t	Î
  g  nameg  new-game C0R1234567  h(   °   ] 445 45 45 45 56   ¨       g  filenamef  eagle-wing.scm
	Q
		R			R	(		S	(		T	(		U	(		V	(		W	(		X	(	#	R		%	R	 		%
  g  nameg  give-status-message C/R289:;<=   h    °   ] 45444
5556 ¨       g  filenamef  eagle-wing.scm
	Z
		[				[			[			[	"		\			\	!		\	)		\	!		\			[	 		
  g  nameg  get-stock-no-string C3R28>:;<=   h    ²   ] 45444	
5556ª       g  filenamef  eagle-wing.scm
	^
		_				_			_			_	$		`			`	!		`	)		`	!		`		 	_	 		 
  g  nameg  get-reserve-no-string C5R8?@ABC2D;   hp   4  ] "  >$  6	$  6	$  6	$  6C$  	$  4	54
56"ÿÿ"ÿÿ ,      g  filenamef  eagle-wing.scm
	b
	
	f				c			g			g				h				c		!	i		#	i			(	j			,	c		0	k		2	k			7	l			;	c		?	m		A	m			C	n		D	c		H	c		L	c		Q	d		U	c			X	e		\	e		^	e		_	e	)	g	e		 		o
  g  nameg  get-base-string C6R28E:;F h       ] 454	56              g  filenamef  eagle-wing.scm
	p
		q				q			q			q	$		r			r	!		r			q	 
		
  g  nameg  get-redeals-string C7RGH    h    À   ]$  4 5$  C6C¸       g  slot-id
		  g  	card-list		   g  filenamef  eagle-wing.scm
	t
		u				v			v			v			u			w			w	 			 	  g  nameg  button-pressed CIRJ'     hX   É   ] 	$  F 	
$  "  54 5$  *4	
5$  "  4	
  >  "  G  "   "   C     Á       g  slot
		S  g  filenamef  eagle-wing.scm
	y
		z			z			{			z			|		#	z		$	}		.	z		3	~		<	~	)	A	~	 		S  g  nameg  fill-tableau-slot CKRG,<LK    hH   ù   ]45$  445>  "  G  "   4 >  "  G   6  ñ       g  
start-slot
		F g  	card-list		F g  end-slot			F  g  filenamef  eagle-wing.scm
 
	 			 		 		 		 		 		 		+ 		F 	 		F	  g  nameg  complete-transaction CMRGJ-N.OP<=        hP  Æ  ] $  C45$  45$  45"  g454455&  N454455$  "  #45$  4455	"  "  "  $  C4
5$  45$  45$  C4455	$  \454455&  B454455$  C45	$  4455CCCCCC    ¾      g  
start-slot
	L g  	card-list	L g  end-slot		L g  t		b  g  t	  L g  t	 ÌH g  t	D  g  filenamef  eagle-wing.scm
 
	 		 		 		 	!	 		 		 		% 		& 		+ 	"	- 		0 		5 		: 	(	< 		= 		@ 	(	H 		L 		M 	 	R 	+	T 	 	U 	#	X 	.	` 	#	a 	 	b 		b 		q 	%	v 	0	x 	%	{ 	"	 	  	%  	0  	%  	"   	 ¬ 	 ² 	! ´ 	 ¸ 	 ¹ 	 Á 	 Å 	 Æ 	 Ì 	 Ø 	 Û 	$ ã 	 æ 	 ê 	 ë 	 ð 	( ò 	 ó 	 ö 	( þ 	 	 	  	+
 	  	# 	. 	# 	  	 	$ 	%) 	0+ 	%. 	"2 	3 	%6 	0> 	%A 	" O	L	  g  nameg  
droppable? CQRQMR     h(   Ç   ]4 5$   456C      ¿       g  
start-slot
		" g  	card-list		" g  end-slot			"  g  filenamef  eagle-wing.scm
 
	  		  		 ¡	(	  ¡	 		"	  g  nameg  button-released CSRT        h   `   ] 
	6      X       g  filenamef  eagle-wing.scm
 £
	
 ¤	 		

  g  nameg  	dealable? CURV       h   i   ] 
	6      a       g  filenamef  eagle-wing.scm
 ¦
	
 §	 		

  g  nameg  do-deal-next-cards CWRW      h      ] 
$  6 C       g  slot-id
		  g  filenamef  eagle-wing.scm
 ©
	 ª		
 ª		 «	 		  g  nameg  button-clicked CXRJH.-)YZ[\,KNOP      hÐ    ]4 5$  "  Q44 55$  @ $  "  ( 	$  	 	
"  $  "   	
"  $ e44 55$  4	5$  4 >  "  G  "  Z4	5$  4 >  "  G  "  74	5$  4 	>  "  G  "  4 
>  "  G  4>  "  G   64	5$  "  44 5544	55$  44 55$  44	55"  $  "  44 5544	55$  +4 >  "  G  4>  "  G   6C4	5$  "  44 5544	55$  44 55$  44	55"  $  "  44 5544	55$  +4 >  "  G  4>  "  G   6C4	5$  "  44 5544	55$  44 55$  44	55"  $  "  44 5544	55$  +4 	>  "  G  4>  "  G   6C4	5$  "  44 5544	55$  44 55$  44	55"  $  "  44 5544	55$  +4 
>  "  G  4>  "  G   6CCC        g  slot
	Î g  t	&	^ g  t		F	[ g  tb g  t; g  tÀê g  to  g  filenamef  eagle-wing.scm
 ®
	 ¯		 ¯		 °		 °		 °		" ¯		& ±		& ±		8 ²		< ²		A ³		F ±		X ´		g ¯		j µ		m µ	)	u µ		v µ		z µ		{ ¶	  ¶	  ·	  ·	%  ·	  ¸	 ¨ ¶	 © ¹	 ¯ ¹	% ´ ¹	 Á º	 Ë ¶	 Ì »	 Ò »	% × »	 ä ½	 ê ½	% ï ½	 ø ¾	 ¿	 À	 À	 Á	" Á	* Á	+ Â	. Â	6 Â	7 Á	; µ	< Ã	? Ã	(G Ã	J Ã	N Ã	O Ä	R Ä	(Z Ä	] Ä	b Ã	p Å	s Å	#{ Å	| Æ	 Æ	( Æ	 Æ	 Å	 Ã	 È	 È	$ È	¥ É	» Ê	¾ Ì	È Ì	Î Í	Ñ Í	Ù Í	Ú Î	Ý Î	å Î	æ Í	ê µ	ë Ï	î Ï	(ö Ï	ù Ï	ý Ï	þ Ð	 Ð	(	 Ð	 Ð	 Ï	 Ñ	" Ñ	#* Ñ	+ Ò	. Ò	(6 Ò	7 Ò	8 Ñ	? Ï	@ Ô	F Ô	$K Ô	T Õ	j Ö	m Ø	w Ø	} Ù	 Ù	 Ù	 Ú	 Ú	 Ú	 Ù	 µ	 Û	 Û	(¥ Û	¨ Û	¬ Û	­ Ü	° Ü	(¸ Ü	» Ü	À Û	Î Ý	Ñ Ý	#Ù Ý	Ú Þ	Ý Þ	(å Þ	æ Þ	ç Ý	î Û	ï à	õ à	$ú à	 á	 â	 ä	& ä	, å	/ å	7 å	8 æ	; æ	C æ	D å	H µ	I ç	L ç	(T ç	W ç	[ ç	\ è	_ è	(g è	j è	o ç	} é	 é	# é	 ê	 ê	( ê	 ê	 é	 ç	 ì	¤ ì	$© ì	² í	È î	 ±	Î  g  nameg  button-double-clicked C]R/^_    h(   {   ] 4>   "  G  45 $  C6        s       g  filenamef  eagle-wing.scm
 ó
	 ô		 õ		 õ		! ö	 		!
  g  nameg  	game-over C`RJ    h     ] 4
5$  z45$  n4	5$  a4	5$  T4	5$  G4		5$  :4	
5$  -4	5$   4	5$  4	5$  	6CCCCCCCCCC      g  filenamef  eagle-wing.scm
 ø
	 ù		 ù		 ú		 ù		 û		! ù		" ü		, ù		- ý		7 ù		8 þ		B ù		C ÿ		M ù		N 		X ù		Y		c ù		d		n ù		t	 	 
  g  nameg  game-won C^RJN.-OP hx     ]
45$  C44 554455$  J44 554455$  C44 55$  4455CCC      g  slot1
		x g  slot2		x g  t		F	v  g  filenamef  eagle-wing.scm

						
				
		
			'	
	(		,		-			0			8			9
		<
		D
		E
		F			F			R		U		]		`		d		e		h		p		s	 		x	  g  nameg  check-a-foundation CaRJH.-bcad   hà   ç  ]4 5$  "  44 55$  44 55$   4564	 	5$  	 	64	 	5$  	 	64	 	5$  	 	64	 	5$  	 	6 $  
	6 	$  
 6C $  
	6 	$  
 6C     ß      g  slot
	 Û  g  filenamef  eagle-wing.scm

											"		#		&		.		1		5		;		C		D		P		Y		Z		f		o		p		|	 	 	 	 	 	 £	 ©	 ®	 ²	 ·	" ¹	 ¿ 	
 Ã 	 É!	
 Î"	 Ò"	
 ×#	# Ù#	 )	 Û  g  nameg  check-to-foundation CdReJb  hP   Ý   ]"   	$   6C4 5$  # 	
$  "ÿÿÖ45$  C 6"ÿÿ¼      Õ       g  slot
		J  g  filenamef  eagle-wing.scm
&
	,	
	,		-		-	
	'		'		#'		((		,'		1)	
	;)		F+	
 		J  g  nameg  check-empty-slot CeRJ<=N.-PObf        hÐ     ] $  "  	
$  "  45$  "  |4455	$  h454455$  K454455$  "  "45$  4455"  "  "  $  		 6	$  
 6C          g  slot
	 Í g  card	 Í g  
check-slot		 Í g  t		n    g  filenamef  eagle-wing.scm
0
	1		1		2		1		3		)1		/4		24		:4		=4		A1		B5		I6		L6		T6		U5		Y1		Z7		a7		b8		e8		m8		n7		n7		|9	 9	 9	 :	 :	" :	 :	 ®1	 ·;	 ¼<	
 À<	 É=	& Ë=	
 '	 Í	  g  nameg  check-to-tableau CfRJH.<=f     hp     ]	4 5$  "  E $  "  1 	$  '44 55$  44 55"  "  $   4 5	6C          g  slot
		l g  t		W  g  filenamef  eagle-wing.scm
@
	A		A		B		B		(C		,C		-D		0D	!	8D		<C		>E		AE	!	IE		JE		[A		`F		jF	 		l  g  nameg  check-tableau CgRJF8hi  h@   Õ   ] 4
5$  &45$  "  	$  
45 CC
45 C  Í       g  filenamef  eagle-wing.scm
I
	J		J		L		L	
	 M		$L		&N		*N		,N		/N	
	4K		8K		:K		=K	 		>
  g  nameg  	dealable? CURdegU    hà   ý  ]45  $   C4	5  $   C45  $   C4	5  $   C4	5  $   C4	5  $   C4		5  $   C4	
5  $   C4	5  $   C4	5  $   C4	5  $   C4	5  $   C6     õ      g  t
	 Ü g  t
	 Ü g  t
	+ Ü g  t
	= Ü g  t
	O Ü g  t
	a Ü g  t
	s Ü g  t
  Ü g  t
  Ü g  t
 © Ü g  t
 » Ü g  t
 Í Ü  g  filenamef  eagle-wing.scm
Q
	R		R		S		R		&T		+R		7U		=R		IV		OR		[W		aR		mX		sR		Y	 R	 Z	 R	 £[	 ©R	 µ\	 »R	 Ç]	 ÍR	 Ü^	 	 Ü
  g  nameg  get-hint C_R      h   Y   ] C    Q       g  filenamef  eagle-wing.scm
`
 		
  g  nameg  get-options CjR  h   q   ]C    i       g  options
		  g  filenamef  eagle-wing.scm
b
 		  g  nameg  apply-options CkR  h   U   ] C    M       g  filenamef  eagle-wing.scm
d
 		
  g  nameg  timeout ClR4minioi>  "  G  pi0iIiSiXi]i`i^i_ijikiliQiUi6    q      g  filenamef  eagle-wing.scm		
		
	!			$	
	&			)	
	.	
	2	
	6	
	
	Q
		Z

u	^
?	b
	p
	t
L	y
¬ 
ñ 
ú 
 £
 ¦
È ©
$b ®
% ó
&Ï ø
(õ
+â
-(&
0+0
1Ð@
3 I
5øQ
6l`
6ôb
7`d
7af
7´h
 '	7´
   C6 