GOOF----LE-8-2.0�w      ]\ 4  h�C      ] g  guile�	 �	g  define-module*�	 �	 �	g  web�	g  server�	g  http�		 �	
g  filenameS�	f  web/server/http.scm�	g  importsS�	g  srfi�	g  srfi-1�	 �	g  selectS�	g  fold�	 �	 �	g  srfi-9�	 �	 �	g  rnrs�	g  bytevectors�	 �	 �	g  request�	 �	 �	g  response�	 �	  �	! �	"! �	#g  ice-9�	$g  poll�	%#$ �	&% �	' "& �	(g  exportsS�	) �	*g  set-current-module�	+* �	,* �	-g  socket�	.g  PF_INET�	/g  SOCK_STREAM�	0g  
setsockopt�	1g  
SOL_SOCKET�	2g  SO_REUSEADDR�	3g  bind�	4g  make-default-socket�	5g  <http-server>�	6g  %make-http-server-procedure�	7g  make-syntax-transformer�	87 �	97 �	:g  make-http-server�	;g  macro�	<g  $sc-dispatch�	=< �	>< �	?g  _�	@g  any�	A?@@@ �	Bg  syntax-object�	Cg  lambda�	Dg  m-WaBjzXLyTZe8jit@UWrmWE-4222�	Eg  top�	FDE �	Gg  ribcage�	Hg  t-4219�	Ig  t-4220�	Jg  t-4221�	KHIJ �	LFFF �	Mf  l-WaBjzXLyTZe8jit@UWrmWE-4227�	Nf  l-WaBjzXLyTZe8jit@UWrmWE-4228�	Of  l-WaBjzXLyTZe8jit@UWrmWE-4229�	PMNO �	QGKLP �	RG �	Sg  x�	TS �	UF �	Vf  l-WaBjzXLyTZe8jit@UWrmWE-4224�	WV �	XGTUW �	Yg  shift�	Zg  	proc-name�	[g  args�	\Z[ �	]E �	^]] �	_f  l-v9ZI7icxzQUmleC7DNgBsg-3379�	`f  l-v9ZI7icxzQUmleC7DNgBsg-3380�	a_` �	bG\^a �	cg  key�	dg  value�	eg  name�	fg  formals�	gg  body�	hcdefg �	i]]]]] �	jf  l-v9ZI7icxzQUmleC7DNgBsg-3366�	kf  l-v9ZI7icxzQUmleC7DNgBsg-3367�	lf  l-v9ZI7icxzQUmleC7DNgBsg-3368�	mf  l-v9ZI7icxzQUmleC7DNgBsg-3369�	nf  l-v9ZI7icxzQUmleC7DNgBsg-3370�	ojklmn �	pGhio �	qg  make-procedure-name�	rq �	s] �	tf  l-v9ZI7icxzQUmleC7DNgBsg-3350�	ut �	vGrsu �	w] �	xf  l-v9ZI7icxzQUmleC7DNgBsg-3349�	yx �	zGTwy �	{FQRXYRRRRbpvz �	|g  hygiene�	}| �	~BC{} �	]QRX � �| � �B-� � �g  poll-idx� �B�� � �g  poll-set� �B�� � ���� � �g  make-struct� �g  m-WaBjzXLyTZe8jit@UWrmWE-4217� ��E � �g  t-3590� �g  t-3589� �g  t-3588� ���� � �g  m-v9ZI7icxzQUmleC7DNgBsg-3591� ��E � ���� � �f  l-v9ZI7icxzQUmleC7DNgBsg-3595� �f  l-v9ZI7icxzQUmleC7DNgBsg-3596� �f  l-v9ZI7icxzQUmleC7DNgBsg-3597� ���� � �G��� � �g  	ctor-args� �� � �f  l-v9ZI7icxzQUmleC7DNgBsg-3571� �� � �G�w� � �g  ctor� �g  field� ��� � �f  l-v9ZI7icxzQUmleC7DNgBsg-3567� �f  l-v9ZI7icxzQUmleC7DNgBsg-3568� ��� � �G�^� � �g  form� �g  	type-name� �g  constructor-spec� �g  field-names� ����� � �]]]] � �f  l-v9ZI7icxzQUmleC7DNgBsg-3556� �f  l-v9ZI7icxzQUmleC7DNgBsg-3557� �f  l-v9ZI7icxzQUmleC7DNgBsg-3558� �f  l-v9ZI7icxzQUmleC7DNgBsg-3559� ����� � �G��� � �g  record-layout� �g  functional-setters� �g  setters� �g  copier� �g  getters� �g  constructor� �g  getter-identifiers� �g  field-identifiers� ��������� � �]]]]]]]] � �f  l-v9ZI7icxzQUmleC7DNgBsg-3516� �f  l-v9ZI7icxzQUmleC7DNgBsg-3514� �f  l-v9ZI7icxzQUmleC7DNgBsg-3512� �f  l-v9ZI7icxzQUmleC7DNgBsg-3510� �f  l-v9ZI7icxzQUmleC7DNgBsg-3508� �f  l-v9ZI7icxzQUmleC7DNgBsg-3506� �f  l-v9ZI7icxzQUmleC7DNgBsg-3504� �f  l-v9ZI7icxzQUmleC7DNgBsg-3502� ��������� � �G��� � �f  l-v9ZI7icxzQUmleC7DNgBsg-3501� �� � �GTw� � ��QRXYR�RRR��R��� � �B��} � �B5� � �B
�} � ������� � �~�� � �g  each-any� �?ˌ� �g  syntax-violation� �� � �� � �f  Wrong number of arguments� �g  identifier?� �� � �� � �]RX � �B6�� � �� � �� � �f  -source expression failed to match any pattern� �g  record-type-vtable� �� � �� � �g  pwpwpw� �g  default-record-printer� �� � �� � �-�� � �g  set-struct-vtable-name!� �� � �� � �g  vtable-offset-user� �� � �� � �g  %http-server?-procedure� �g  http-server?� �?@ � �g  m-WaBjzXLyTZe8jit@UWrmWE-4239� ��E � �g  t-4238� �� � �� � �f  l-WaBjzXLyTZe8jit@UWrmWE-4244� �� � �G��� � �f  l-WaBjzXLyTZe8jit@UWrmWE-4241� �� � �GT�� � ���R�YRRRRbpvz � �BC�} � �g  obj� �g  t-3831� �g  t-3825� �g  t-3826� �g  t-3827� �g  t-3830� �g  t-3829� �g  t-3828� �������� � g  m-v9ZI7icxzQUmleC7DNgBsg-3832� E � �f  l-v9ZI7icxzQUmleC7DNgBsg-3836�f  l-v9ZI7icxzQUmleC7DNgBsg-3837�f  l-v9ZI7icxzQUmleC7DNgBsg-3838�f  l-v9ZI7icxzQUmleC7DNgBsg-3839�f  l-v9ZI7icxzQUmleC7DNgBsg-3840�f  l-v9ZI7icxzQUmleC7DNgBsg-3841�	f  l-v9ZI7icxzQUmleC7DNgBsg-3842�
	 �G�
 �g  	copier-id� �f  l-v9ZI7icxzQUmleC7DNgBsg-3823� �Gw �g  	ctor-name� �f  l-v9ZI7icxzQUmleC7DNgBsg-3815� �Gw �� �f  l-v9ZI7icxzQUmleC7DNgBsg-3813� �Gw �g  layout� �f  l-v9ZI7icxzQUmleC7DNgBsg-3811� �Gw �g  
immutable?�  �!f  l-v9ZI7icxzQUmleC7DNgBsg-3809�"! �#G w" �$g  field-count�%$ �&f  l-v9ZI7icxzQUmleC7DNgBsg-3807�'& �(G%w' �)g  
getter-ids�*) �+f  l-v9ZI7icxzQUmleC7DNgBsg-3804�,+ �-G*w, �.g  	field-ids�/. �0f  l-v9ZI7icxzQUmleC7DNgBsg-3801�10 �2G/w1 �3g  predicate-name�4g  
field-spec�5���34 �6]]]]]] �7f  l-v9ZI7icxzQUmleC7DNgBsg-3788�8f  l-v9ZI7icxzQUmleC7DNgBsg-3789�9f  l-v9ZI7icxzQUmleC7DNgBsg-3790�:f  l-v9ZI7icxzQUmleC7DNgBsg-3791�;f  l-v9ZI7icxzQUmleC7DNgBsg-3792�<f  l-v9ZI7icxzQUmleC7DNgBsg-3793�=789:;< �>G56= �?��R�YRRRRRRRRR#R(R-R2>�� �@B�?} �A@ �Bg  and�CBB?} �Dg  struct?�EBD?} �FE@ �Gg  eq?�HBG?} �Ig  struct-vtable�JBI?} �KJ@ �L]�R� �MB5L� �NHKM �OCFN �P�AO �Q]R� �RB�Q� �Sg  throw-bad-struct�TS �US �Vg  http-socket�Wg  %http-socket-procedure�Xg  free-id�Yg  
%%on-error�Zg  m-WaBjzXLyTZe8jit@UWrmWE-4251�[ZE �\[ �]f  l-WaBjzXLyTZe8jit@UWrmWE-4253�^] �_GT\^ �`[R_YRRRRbpvz �aBY`} �bXa �cb@ �dg  %%type�eg  t-3614�fg  t-3615�gg  t-3616�hg  t-3617�ig  t-3618�jg  t-3619�kg  t-3620�lefghijk �mg  m-v9ZI7icxzQUmleC7DNgBsg-3621�nmE �onnnnnnn �pf  l-v9ZI7icxzQUmleC7DNgBsg-3625�qf  l-v9ZI7icxzQUmleC7DNgBsg-3626�rf  l-v9ZI7icxzQUmleC7DNgBsg-3627�sf  l-v9ZI7icxzQUmleC7DNgBsg-3628�tf  l-v9ZI7icxzQUmleC7DNgBsg-3629�uf  l-v9ZI7icxzQUmleC7DNgBsg-3630�vf  l-v9ZI7icxzQUmleC7DNgBsg-3631�wpqrstuv �xGlow �yg  getter�zg  index�{yz �|f  l-v9ZI7icxzQUmleC7DNgBsg-3612�}f  l-v9ZI7icxzQUmleC7DNgBsg-3613�~|} �G{^~ ���) ��]]] ��f  l-v9ZI7icxzQUmleC7DNgBsg-3607��f  l-v9ZI7icxzQUmleC7DNgBsg-3608��f  l-v9ZI7icxzQUmleC7DNgBsg-3609����� ��G��� ���R_YRxRRRR��� ��Bd�} ��X� ��?c�@ ��g  ck��g  err��g  s���� ��[[ ��f  l-WaBjzXLyTZe8jit@UWrmWE-4256��f  l-WaBjzXLyTZe8jit@UWrmWE-4257���� ��G��� ��[�R_YRRRRbpvz ��B��} ��g  quote��B��} ��]�R_ ��B5�� ���� ��� ��g  %%index��B��} ��X� ��?c�@ ��f  l-WaBjzXLyTZe8jit@UWrmWE-4261��f  l-WaBjzXLyTZe8jit@UWrmWE-4262���� ��G��� ��[�R_YRRRRbpvz ��B��} ��B��} ���R_ ��B
�� ���� ��� ��g  %%copier��B��} ��X� ��?c�@ ��f  l-WaBjzXLyTZe8jit@UWrmWE-4266��f  l-WaBjzXLyTZe8jit@UWrmWE-4267���� ��G��� ��[�R_YRRRRbpvz ��B��} ��B��} ��g  %%<http-server>-set-fields��]�R_ ��B��� ���� ��� ��g  t-4250��� ��f  l-WaBjzXLyTZe8jit@UWrmWE-4271��� ��G�\� ��[�R_YRRRRbpvz ��BC�} ����R_YRxRRRR��� ��B��} ��� ��g  if��B��} ��BG�} ��BI�} ���� ��]�R_ ��B5�� ����� ��g  
struct-ref��B��} ���R_ ��B
�� ����� ��BS�} ��B��} ��BV�� ���� ����� ������ ����� ��]R_ ��BW�� ��g  http-poll-idx��g  %http-poll-idx-procedure��g  m-WaBjzXLyTZe8jit@UWrmWE-4278���E ��� ��f  l-WaBjzXLyTZe8jit@UWrmWE-4280��� ��GT�� ���R�YRRRRbpvz ��BY�} ��X� ���@ ���R�YRxRRRR��� ��Bd�} ��X� ��?��@ ���� ��f  l-WaBjzXLyTZe8jit@UWrmWE-4283��f  l-WaBjzXLyTZe8jit@UWrmWE-4284���� ��G��� ����R�YRRRRbpvz ��B��} ��B��} ��]�R� ��B5�� ���� ��� ��B��} ��X� ��?��@ ��f  l-WaBjzXLyTZe8jit@UWrmWE-4288��f  l-WaBjzXLyTZe8jit@UWrmWE-4289���� ��G��� ����R�YRRRRbpvz ��B��} � B��} ��R� �B� �  � �B��} �X �?�@ �f  l-WaBjzXLyTZe8jit@UWrmWE-4293�	f  l-WaBjzXLyTZe8jit@UWrmWE-4294�
	 �G��
 ��R�YRRRRbpvz �B�} �B�} �]R� �B�� � � �g  t-4277� �f  l-WaBjzXLyTZe8jit@UWrmWE-4298� �G� ��R�YRRRRbpvz �BC} ��R�YRxRRRR��� �B�} � �B�} �BG} �BI} �  �!]R� �"B5!� �# " �$B�} �%R� �&B%� �'$& �(BS} �)B�} �*B�!� �+)* �,(+ �-#', �.- �/]R� �0B�/� �1g  http-poll-set�2g  %http-poll-set-procedure�3g  m-WaBjzXLyTZe8jit@UWrmWE-4305�43E �54 �6f  l-WaBjzXLyTZe8jit@UWrmWE-4307�76 �8GT57 �94R8YRRRRbpvz �:BY9} �;X: �<;@ �=�R8YRxRRRR��� �>Bd=} �?X> �@?<?@ �A44 �Bf  l-WaBjzXLyTZe8jit@UWrmWE-4310�Cf  l-WaBjzXLyTZe8jit@UWrmWE-4311�DBC �EG�AD �F4ER8YRRRRbpvz �GB�F} �HB�F} �I]ER8 �JB5I� �KHJ �LK �MB�=} �NXM �O?<N@ �Pf  l-WaBjzXLyTZe8jit@UWrmWE-4315�Qf  l-WaBjzXLyTZe8jit@UWrmWE-4316�RPQ �SG�AR �T4SR8YRRRRbpvz �UB�T} �VB�T} �WSR8 �XB	W� �YVX �ZY �[B�=} �\X[ �]?<\@ �^f  l-WaBjzXLyTZe8jit@UWrmWE-4320�_f  l-WaBjzXLyTZe8jit@UWrmWE-4321�`^_ �aG�A` �b4aR8YRRRRbpvz �cB�b} �dB�b} �e]aR8 �fB�e� �gdf �hg �ig  t-4304�ji �kf  l-WaBjzXLyTZe8jit@UWrmWE-4325�lk �mGj5l �n4mR8YRRRRbpvz �oBCn} �p�mR8YRxRRRR��� �qB�p} �rq �sB�p} �tBGp} �uBIp} �vuq �w]mR8 �xB5w� �ytvx �zB�p} �{mR8 �|B	{� �}zq| �~BSp} �B�p} ��B1w� ��� ��~q� ��sy}� ��or� ��]R8 ��B2�� ��g  each��@@ ���� ��@����@����@����g  %%set-fields��g  dummy��g  check?��g  expr�����y� ��g  m-WaBjzXLyTZe8jit@UWrmWE-4332���E ������� ��f  l-WaBjzXLyTZe8jit@UWrmWE-4337��f  l-WaBjzXLyTZe8jit@UWrmWE-4338��f  l-WaBjzXLyTZe8jit@UWrmWE-4339��f  l-WaBjzXLyTZe8jit@UWrmWE-4340��f  l-WaBjzXLyTZe8jit@UWrmWE-4341������� ��G��� ��� ��f  l-WaBjzXLyTZe8jit@UWrmWE-4334��� ��GT�� ��g  t-3645��g  t-3647��g  t-3646����� ��g  m-v9ZI7icxzQUmleC7DNgBsg-3648���E ����� ��f  l-v9ZI7icxzQUmleC7DNgBsg-3652��f  l-v9ZI7icxzQUmleC7DNgBsg-3653��f  l-v9ZI7icxzQUmleC7DNgBsg-3654����� ��G��� ��f  l-v9ZI7icxzQUmleC7DNgBsg-3642��f  l-v9ZI7icxzQUmleC7DNgBsg-3643��f  l-v9ZI7icxzQUmleC7DNgBsg-3644����� ��G��� ����R�YR�RRR��� ��B��} ��]�R� ��B5�� ��BV�� ��B��� ��B1�� ����� ��g  map��� ��� ��g  list��g  set-http-poll-idx!��g  %set-http-poll-idx!-procedure��?@@ ��g  m-WaBjzXLyTZe8jit@UWrmWE-4352���E ��g  t-4350��g  t-4351���� ���� ��f  l-WaBjzXLyTZe8jit@UWrmWE-4357��f  l-WaBjzXLyTZe8jit@UWrmWE-4358���� ��G��� ��� ��f  l-WaBjzXLyTZe8jit@UWrmWE-4354��� ��GT�� ����R�YRRRRbpvz ��BC�} ��g  t-3679��g  t-3680���� ��g  m-v9ZI7icxzQUmleC7DNgBsg-3681���E ���� ��f  l-v9ZI7icxzQUmleC7DNgBsg-3685��f  l-v9ZI7icxzQUmleC7DNgBsg-3686���� ��G��� ��g  setter��ey� ��f  l-v9ZI7icxzQUmleC7DNgBsg-3673��f  l-v9ZI7icxzQUmleC7DNgBsg-3674��f  l-v9ZI7icxzQUmleC7DNgBsg-3675����� ��G��� ��4z ��f  l-v9ZI7icxzQUmleC7DNgBsg-3664��f  l-v9ZI7icxzQUmleC7DNgBsg-3665���� ��G�^� ��g  field-specs���� ��f  l-v9ZI7icxzQUmleC7DNgBsg-3660��f  l-v9ZI7icxzQUmleC7DNgBsg-3661���� ��G�^� ����R�YR��R�R��� ��B��} ��g  val��B��} ���� ��B��} ��BG�} ��BI�} ���� ��]�R� ��B5�� ����� ��g  struct-set!��B��} ���R� ��B�� ������ ��BS�} ��B��} ��B��� � �� ���  ���� ��� �]R� �B�� �g  POLLHUP�g  POLLERR�g  *error-events*�	g  POLLIN�
g  *read-events*�g  *events*�g  hostS�
��g  familyS���g  addrS�	��g  portS�	��g  socketS�	�� �g  AF_INET�g  	inet-pton�g  INADDR_LOOPBACK�g  listen�g  	sigaction�g  SIGPIPE�g  SIG_IGN�g  make-empty-poll-set�g  poll-set-add!� g  	http-open�!g  write-response�"g  build-response�#g  versionS�$
��%g  codeS�&g  headersS�'g  content-length�('
��)( �*g  bad-request�+g  poll-set-revents�,g  
<poll-set>�-%, �.%, �/g  poll-set-nfds�0g  accept�1g  poll-set-port�2g  setvbuf�3g  _IOFBF�4g  	SO_SNDBUF�5g  throw�6g  	interrupt�7g  poll-set-remove!�8g  eof-object?�9g  	peek-char�:g  
close-port�;g  with-throw-handler�<g  read-request�=g  read-request-body�>g  catch�?g  format�@g  current-error-port�Af  In ~a:
�Bg  port�C*B �Dg  print-exception�E:B �Fg  	http-read�Gg  
<response>�HG �IG �Jg  response-version�Kg  response-code�Lg  memq�Mg  close�Ng  response-connection�Og  
keep-alive�Pg  keep-alive?�Qg  response-port�Rg  bytevector?�Sg  write-response-body�Tg  error�Uf  Expected a bytevector for body�Vg  force-output�Wg  
http-write�Xg  
http-close�Yg  server-impl�Z!Y �[!Y �C 5     h(/  /  ] 4	
'()5 4, >  "  G   -./0123  h@   �   ]4
54>  "  G  4 >  "  G  C�       g  family
		@ g  addr		@ g  port			@ g  sock			@  g  filenamef  web/server/http.scm�
	(
��		)	��		)	��		*	��	&	+	�� 		@	  g  nameg  make-default-socket� C4R5       h   �   ] � C  �       g  socket
		 g  poll-idx		 g  poll-set			  g  filenamef  web/server/http.scm�
	.
�� 			  g  nameg  %make-http-server-procedure� C6R49:;>A�     h   V   ]  C  N       g  t-4219
		 g  t-4220		 g  t-4221			  			   C��:�      h   V   ]L 6    N       g  a
		  g  filenamef  web/server/http.scm�		.
�� 		   C?�  h   F   ] L 6>       g  filenamef  web/server/http.scm�		.
�� 		
   C�    h      ] C          		
   C��        hp   �   ]4 5$  @4 5$   O @4 5$  4 O ?$  @	
 6	
 6         g  x
		n g  tmp		n g  tmp		"	n g  tmp		>	n  g  filenamef  web/server/http.scm�
	.
�� 		n   C5:R���5�  4� 5>  "  G   	�6i�  5R5      h   {   ] �$   ��CC      s       g  obj
		  g  filenamef  web/server/http.scm�
	.
�� 		  g  nameg  %http-server?-procedure� C�R49�;>�P       h   .   ]  C      &       g  t-4238
		
  		
   C����      h   V   ]L 6    N       g  a
		  g  filenamef  web/server/http.scm�		.
�� 		   C?�  h   F   ] L 6>       g  filenamef  web/server/http.scm�		.
�� 		
   CR   h      ] C          		
   C��        hp   �   ]4 5$  @4 5$   O @4 5$  4 O ?$  @	
 6	
 6         g  x
		n g  tmp		n g  tmp		"	n g  tmp		>	n  g  filenamef  web/server/http.scm�
	.
�� 		n   C5�R5UV        h   x   ] �&   
�C 6p       g  s
		  g  filenamef  web/server/http.scm�
	.
�� 		  g  nameg  %http-socket-procedure� CWR49V;>���    h   :   ]��C     2       g  err
		 g  s		  			   C��� h   :   ]��C     2       g  err
		 g  s		  			   C��� h   :   ]��C     2       g  err
		 g  s		  			   C��     h   .   ]  C      &       g  t-4250
		
  		
   C��V�     h   V   ]L 6    N       g  a
		  g  filenamef  web/server/http.scm�		.
�� 		   C?�  h   F   ] L 6>       g  filenamef  web/server/http.scm�		.
�� 		
   C�   h      ] C          		
   C��        h�   �   ]14 5$  @4 5$  @4 5$  @4 5$  	@4 
5$   O @4 5$  4 O ?$  @ 6 6     �       g  x
	 � g  tmp	 � g  tmp		" � g  tmp		9 � g  tmp		P � g  tmp		g � g  tmp	 � �  g  filenamef  web/server/http.scm�
	.
�� 	 �   C5VR5U�   h   z   ] �&   �C 6r       g  s
		  g  filenamef  web/server/http.scm�
	.
�� 		  g  nameg  %http-poll-idx-procedure� C�R49�;>���  h   :   ]��C     2       g  err
		 g  s		  			   C�� h   :   ]��C     2       g  err
		 g  s		  			   C h   :   ]��C     2       g  err
		 g  s		  			   C�.     h   .   ]  C      &       g  t-4277
		
  		
   C����     h   V   ]L 6    N       g  a
		  g  filenamef  web/server/http.scm�		.
�� 		   C?�  h   F   ] L 6>       g  filenamef  web/server/http.scm�		.
�� 		
   C0   h      ] C          		
   C��        h�   �   ]14 5$  @4 5$  @4 5$  @4 5$  	@4 
5$   O @4 5$  4 O ?$  @ 6 6     �       g  x
	 � g  tmp	 � g  tmp		" � g  tmp		9 � g  tmp		P � g  tmp		g � g  tmp	 � �  g  filenamef  web/server/http.scm�
	.
�� 	 �   C5�R5U1   h    z   ] �&   	�C 6       r       g  s
		  g  filenamef  web/server/http.scm�
	.
�� 		  g  nameg  %http-poll-set-procedure� C2R491;>@GL  h   :   ]��C     2       g  err
		 g  s		  			   COUZ h   :   ]��C     2       g  err
		 g  s		  			   C]ch h   :   ]��C     2       g  err
		 g  s		  			   C��     h   .   ]  C      &       g  t-4304
		
  		
   C��1�     h   V   ]L 6    N       g  a
		  g  filenamef  web/server/http.scm�		.
�� 		   C?�  h   F   ] L 6>       g  filenamef  web/server/http.scm�		.
�� 		
   C�   h      ] C          		
   C��        h�   �   ]14 5$  @4 5$  @4 5$  @4 5$  	@4 
5$   O @4 5$  4 O ?$  @ 6 6     �       g  x
	 � g  tmp	 � g  tmp		" � g  tmp		9 � g  tmp		P � g  tmp		g � g  tmp	 � �  g  filenamef  web/server/http.scm�
	.
�� 	 �   C51R49�;>������      h    v   ]45�����C   n       g  dummy
		 g  check?		 g  s			 g  getter			 g  expr			  			   C��   h(   �   ]	4 5$  @ 6      �       g  x
		" g  tmp		"  g  filenamef  web/server/http.scm�
	.
�� 		"  g  
macro-typeg  syntax-rules�g  patternsg  check?g  sg  getterg  expr g  ...   C5�R5U�     h    �   ] �&   �C 6      �       g  s
		 g  val		  g  filenamef  web/server/http.scm�
	.
�� 			  g  nameg  %set-http-poll-idx!-procedure� C�R49�;>�       h   B   ]  C    :       g  t-4350
		 g  t-4351		  			   C���� h   V   ]L 6    N       g  a
		  g  filenamef  web/server/http.scm�		.
�� 		   C?�  h   F   ] L 6>       g  filenamef  web/server/http.scm�		.
�� 		
   C   h      ] C          		
   C��        hp   �   ]4 5$  @4 5$   O @4 5$  4 O ?$  @	
 6	
 6         g  x
		n g  tmp		n g  tmp		"	n g  tmp		>	n  g  filenamef  web/server/http.scm�
	.
�� 		n   C5�Rii�R	i
Ri
i�R45   h�   g  -  /     0   3  #   #  #   $  4 5"  #  �#  454 �>  "  G  4	>  "  G  4
5 4>  "  G  
� C      _      g  host
	 � g  family	 � g  addr		 � g  port		 � g  socket		 � g  poll-set	 � �  g  filenamef  web/server/http.scm�
	:
��	2	=	��	3	>	��	U	A	��	b	B	��	w	C	�� �	D	�� �	D	�� �	E	�� �	F	�� 	 �

g  hostS
�g  familyS�g  addrS	�g  portS	�g  socketS	�   g  nameg  	http-open� C R!"#$%&)    h    �   ]4�5 6      �       g  port
		  g  filenamef  web/server/http.scm�
	H
��		I	��		I	,��		J	,��		I	��		I	�� 		  g  nameg  bad-request� C*R5U1+$./0123014�56789:;<=  h   y   ]4L 5 L  4 5Dq       g  req
			  g  filenamef  web/server/http.scm�
	}	��		~	��			~	��	 �	��			�� 		
   C>*    h   P   ] L 6H       g  filenamef  web/server/http.scm�
 �	��	 �	 �� 		
   C?@ACD     h0   j   - 1 3 445 >  "  G  45  6b       g  k
			0 g  args			0  g  filenamef  web/server/http.scm�
 �	�� 			0
   C:       h   P   ] L 6H       g  filenamef  web/server/http.scm�
 �	��	 �	 �� 		
   C?@AED     h0   j   - 1 3 445 >  "  G  45  6b       g  k
			0 g  args			0  g  filenamef  web/server/http.scm�
 �	�� 			0
   C   h8   |   - 1 3 4L O >  "  G  L O 6       t       g  k
			1 g  args			1  g  filenamef  web/server/http.scm�
 �	��	
 �	��	1 �	�� 			1
   C�      h�  �  ]) �&  	 	�"  	4 5" �45
�$  �
�$  34>  "  G  �&  �"  	45�"����
�$  �4	4
554�>  "  G  4�0 >  "  G  4�>  "  G  4>  "  G  �&  �"  	45�"�� �&   �"  4 >  "  G  6
�$  	�"���45� �&   �"  4 >  "  G  4455$  4>  "  G  �"��yO O 6 �&   �"  	4 5"��F   �      g  server
	� g  poll-set	� g  idx		#� g  revents		,� g  client	 � g  port	M� g  val	R  g  filenamef  web/server/http.scm�
	N
��		O	��		O	��	#	P	��	$	Q	��	,	Q	��	1	S	
��	6	R	��	9	V	��	>	U	
��	?	X	��	S	Y	��	k	Y	��	q	Y	��	v	Z	��	w	Z	��	|	U	
��	}	b	�� �	b	"�� �	b	�� �	b	�� �	d	�� �	d	�� �	d	�� �	f	�� �	f	�� �	f	<�� �	f	�� �	g	�� �	g	&�� �	g	�� �	h	�� �	i	�� �	i	��	i	��	\	��1	]	��3	]	��6	j	
��;	R	��>	l	��D	l	
��E	p	��M	p	
��R	s	'��R	s	���	u	���	u	���	u	���	t	���	w	���	x	���	x	���	{	���	P	���	P	���	P	�� :	�  g  nameg  	http-read� CFRIUJKLMNO 	   h�     ] �&   
�"  	4 5 �&   �"  	4 5��$  "   �&   �"  	4 5��$  C��$  4��$  44 55�C
�$  4 56CCC     w      g  response
	 � g  v	 � g  t		<	j g  key		q � g  key		~ �  g  filenamef  web/server/http.scm�
 �
��	 �	��	 �	��	! �	��	< �	��	< �		��	L �	��	g �	��	n �	��	q �	��	q �		��	~ �	��	~ �	�� � �	�� � �	�� � �	%�� � �	�� � �	�� � �	�� � �	�� � �	%�� � �	�� 	 �  g  nameg  keep-alive?� CPR!IUQRSTUPV51:     h�   �  ]45�&  		�"  	45$  ;45$  4>  "  G  "  4>  "  G  "   4	5$  E4
>  "  G  4 �&  	 	�"  	4 5>  "  G  "  4>  "  G  D  �      g  server
	 � g  client	 � g  response		 � g  body		 � g  response		 � g  port		( �  g  filenamef  web/server/http.scm�
 �
��	 �	��	 �	��	 �	��	( �	��	0 �	��	1 �	��	; �	��	< �	��	T �	��	X �	��	_ �	��	l �	��	v �	��	w �	�� � �	�� � �	�� � �	�� � �	�� � �	�� 	 �	  g  nameg  
http-write� CWR5U1:7./       hp     ] �&  	 	�"  	4 5"  -
�$  #44�5>  "  G  �"���C�&  �"  	45"���      g  server
		p g  poll-set		p g  n		#	P  g  filenamef  web/server/http.scm�
 �
��	 �	��	 �	��	# �	��	& �	
��	+ �	��	, �	��	/ �	��	6 �	3��	8 �	��	= �	��	H �	��	N �	��	P �	��	S �	��	p �	�� 		p  g  nameg  
http-close� CXR iFiWiXi [ �  RC  '      g  m
		, g  rtd
� g  open
.�/! g  read.�/! g  write	.�/! g  close	.�/!  g  filenamef  web/server/http.scm�		
��[	(
��1	.
��	5	��	5
��	6
��(	7	��,	7
���	:
��d	H
��(0	N
��*� �
��-1 �
��.� �
��.� �
�� 	/&
   C6 