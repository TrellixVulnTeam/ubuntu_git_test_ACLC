GOOF----LE-8-2.0y      ] A 4     h¼      ] g  guile¤	 ¤	g  process-use-modules¤	 ¤	 ¤	g  	aisleriot¤	g  	interface¤	 ¤		 ¤	
g  api¤	
 ¤	 ¤	g  initialize-playing-area¤	g  set-ace-low¤	g  make-deck-list-ace-low¤	g  club¤	g  DECK¤	g  shuffle-deck¤	g  add-normal-slot¤	g  add-blank-slot¤	g  add-carriage-return-slot¤	g  add-extended-slot¤	g  down¤	g  	add-card!¤	g  make-visible¤	g  	make-card¤	g  ace¤	g  give-status-message¤	g  new-game¤	g  set-statusbar-message¤	g  get-stock-no-string¤	 g  string-append¤	!g  _¤	"f  Stock left:¤	#f   ¤	$g  number->string¤	%g  length¤	&g  	get-cards¤	'g  empty-slot?¤	(g  button-pressed¤	)g  	get-value¤	*g  get-top-card¤	+g  
droppable?¤	,g  move-n-cards!¤	-g  add-to-score!¤	.g  button-released¤	/g  
flip-stock¤	0g  button-clicked¤	1g  button-double-clicked¤	2g  game-won¤	3g  get-hint¤	4g  game-continuable¤	5g  check-to-foundation¤	6g  	hint-move¤	7f  Move card from waste¤	8g  check-waste¤	9f  Deal another card¤	:g  	dealable?¤	;g  get-options¤	<g  apply-options¤	=g  timeout¤	>g  set-features¤	?g  droppable-feature¤	@g  
set-lambda¤C 5       hp  ß   ] 4	 >  "  G     hà  d  ] 4>   "  G  4>   "  G  4	5 4>   "  G  4>  "  G  4>  "  G  4>   "  G  4>  "  G  4>  "  G  4>  "  G  4>  "  G  4	>   "  G  4>   "  G  4>   "  G  4>   "  G  4
>  "  G  4
>  "  G  4
>  "  G  4
>  "  G  4	4455>  "  G  4	44	55>  "  G  4	44	55>  "  G  4	44	55>  "  G  4>   "  G  		 C       \      g  filenamef  hopscotch.scm
	
							#			.			/			?			Q			T			Y			b			r			u			z		 		 		 		 		 		 		 ¥		 ¨		 ­		 ¶	 	 Æ	!	 Ö	"	 æ	#	 ö	$	 ù	$	 	$			%		%		%		&		&	&	&	/	'	2	'	9	'	B	)	G	)	J	)	T	)	Y	)	b	*	g	*	j	*	t	*	y	*		+		+		+		+		+	¢	,	§	,	ª	,	´	,	¹	,	Â	.	Ø	0	 >	Ù
  g  nameg  new-game CR h   o   ] 45 6     g       g  filenamef  hopscotch.scm
	2
		3			3	 		
  g  nameg  give-status-message CR !"#$%&    h    ¯   ] 45444
5556 §       g  filenamef  hopscotch.scm
	5
		6				6			6			6	"		7			7	!		7	)		7	!		7			6	 		
  g  nameg  get-stock-no-string CR'%      h8   Ö   ]
4 5$  C45$   $  C 	CC     Î       g  slot-id
		3 g  	card-list		3 g  t		 	1  g  filenamef  hopscotch.scm
	9
		:			:			;	
		;			:		 	<		 	<		0	=	 
		3	  g  nameg  button-pressed C(R)*       hX   <  ]"   $  	$  CCC$  -	$   45	4455	C"ÿÿ´"ÿÿ°  4      g  
start-slot
		V g  	card-list		V g  end-slot			V  g  filenamef  hopscotch.scm
	?
	
	D			@			E			D				@		!	@		%	@		*	A		.	@			/	B		4	B		6	B		9	B		<	C		=	C	&	@	C	1	H	C	&	I	C		L	C		M	B		 		V	  g  nameg  
droppable? C+R+,-       hH   á   ]4 5$  04 >  "  G  $  	$  6CCC     Ù       g  
start-slot
		C g  	card-list		C g  end-slot			C  g  filenamef  hopscotch.scm
	I
		J			J			L		+	M		/	M		4	M	 	8	M		=	N	 
		C	  g  nameg  button-released C.R'/    h       ] 
$  45$  
6CC        g  slot-id
		  g  filenamef  hopscotch.scm
	R
		S		
	S			T			S			U	 		  g  nameg  button-clicked C0R   h   w   ]C    o       g  slot-id
		  g  filenamef  hopscotch.scm
	W
 		  g  nameg  button-double-clicked C1R23    h(   |   ] 4>   "  G  45 $  C6        t       g  filenamef  hopscotch.scm
	Z
		[			\			\		!	]	 		!
  g  nameg  game-continuable C4R'   hH   ¬   ] 4
5$  945$  -4	5$   4	5$  4	5$  		6CCCCC ¤       g  filenamef  hopscotch.scm
	_
		`			`			a			`			b		!	`		"	c		,	`		-	d		7	`		=	e	 		G
  g  nameg  game-won C2R5')*6   hÈ   ê  ] 		$  "   $  	 	"  $  C	$  	 	64 5$  "  S45$  "  4455	$  "  $44 55	4455	$  	 6 6       â      g  slot-id
	 Á g  foundation-id	 Á g  t			) g  t		H « g  t		t ¨  g  filenamef  hopscotch.scm
	g
		h			h				i			i		!	j		-	h		4	l			8	h		=	m		A	m			B	n		H	n			V	o		`	o		f	p		i	p	 	q	p		t	p		t	n		 	q	 	q	( 	q	 	q	 	r	  	s	  	s	+ 	s	   	r	 £	r	 ¤	q	 ¥	q	 ¯	h	 ¶	u	& ¸	u		 Á	v	 %	 Á	  g  nameg  check-to-foundation C5R'5!7       h0      ] 45$  C4	5$  	6
45 C          g  filenamef  hopscotch.scm
	x
		y				y			{				y		!	|			#	}		'	}		)	}		,	}	 		-
  g  nameg  check-waste C8R'!9    h       ] 4
5$  C
45 C             g  filenamef  hopscotch.scm
	
	 		 		 		 		 		 	 		
  g  nameg  	dealable? C:R58:        h0       ]4		5  $   C45   $   C6              g  t
		* g  t
		*  g  filenamef  hopscotch.scm
 
	 		 		 		 		* 	 		*
  g  nameg  get-hint C3R   h   X   ] C    P       g  filenamef  hopscotch.scm
 
 		
  g  nameg  get-options C;R   h   p   ]C    h       g  options
		  g  filenamef  hopscotch.scm
 
 		  g  nameg  apply-options C<R   h   T   ] C    L       g  filenamef  hopscotch.scm
 
 		
  g  nameg  timeout C=R4>i?i>  "  G  @ii(i.i0i1i4i2i3i;i<i=i+i6     ×       g  filenamef  hopscotch.scm		
	
"	2
	5
9	9
ç	?

,	I

û	R
	W
G	Z
O	_
	g

	x
Î	
» 
+ 
³ 
 
  
k 
 	k
   C6 