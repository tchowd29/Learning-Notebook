from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import os

root = Tk()
root.title('Learn Japanese')
root.geometry("1500x720")

my_notebook = ttk.Notebook(root)
my_notebook.pack()

my_notebook2 = ttk.Notebook(root)
my_notebook2.pack()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# the designated commands for the buttons
def show():
    my_notebook2.add(Vowels, text="Vowels")
    my_notebook2.add(kcolumn, text="K-Column")
    my_notebook2.add(scolumn, text="S-Column")
    my_notebook2.add(tcolumn, text="T-Column")
    my_notebook2.add(ncolumn, text="N-Column")
    my_notebook2.add(hcolumn, text="H-Column")
    my_notebook2.add(mcolumn, text="M-Column")
    my_notebook2.add(ycolumn, text="Y-Column")
    my_notebook2.add(rcolumn, text="R-Column")
    my_notebook2.add(wcolumn, text="W-Column & N")

def show2():
    my_notebook2.add(gcolumn, text="G-Column")
    my_notebook2.add(zcolumn, text="Z-Column")
    my_notebook2.add(dcolumn, text="D-Column")
    my_notebook2.add(bcolumn, text="B-Column")
    my_notebook2.add(pcolumn, text="P-Column")

def show3():
    my_notebook2.add(Combinations1, text="Combinations")
    my_notebook2.add(specialcase, text="Special Combinations")

def show4():
    my_notebook2.add(radical24, text="Radical 1-24")
    my_notebook2.add(radical48, text="Radical 25-48")
    my_notebook2.add(radical72, text="Radical 49-72")
    my_notebook2.add(radical96, text="Radical 73-96")
    my_notebook2.add(radical120, text="Radical 97-120")
    my_notebook2.add(radical144, text="Radical 121-144")
    my_notebook2.add(radical168, text="Radical 145-168")
    my_notebook2.add(radical192, text="Radical 169-192")
    my_notebook2.add(radical214, text="Radical 193-214")
    

def hide():
    for i in range(26):
        my_notebook2.hide(i)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Creates the box for everything:
HiraKana = Frame(my_notebook, width=500, height=250)
Dakuten = Frame(my_notebook, width=500, height=250)
Combohirakana = Frame(my_notebook, width=500, height=250)
smalltsu = Frame(my_notebook, width=500, height=250)
Kanji = Frame(my_notebook, width=500, height=250)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Creates the tabs:
my_notebook.add(HiraKana, text="Hiragana & Katakana")
my_notebook.add(Dakuten, text="Dakuten")
my_notebook.add(Combohirakana, text="Combination Hiragana & Katakana")
my_notebook.add(smalltsu, text="Double Consonant & Long Vowels")
my_notebook.add(Kanji, text="Kanji & Radicals")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Designates the subtabs in each major section:
if HiraKana:
    Vowels = Frame(my_notebook2, width=500, height=500)
    kcolumn = Frame(my_notebook2, width=500, height=500)
    scolumn = Frame(my_notebook2, width=500, height=500)
    tcolumn = Frame(my_notebook2, width=500, height=500)
    ncolumn = Frame(my_notebook2, width=500, height=500)
    hcolumn = Frame(my_notebook2, width=500, height=500)
    mcolumn = Frame(my_notebook2, width=500, height=500)
    ycolumn = Frame(my_notebook2, width=500, height=500)
    rcolumn = Frame(my_notebook2, width=500, height=500)
    wcolumn = Frame(my_notebook2, width=500, height=500)

if Dakuten:
    gcolumn = Frame(my_notebook2, width=500, height=500)
    zcolumn = Frame(my_notebook2, width=500, height=500)
    dcolumn = Frame(my_notebook2, width=500, height=500)
    bcolumn = Frame(my_notebook2, width=500, height=500)
    pcolumn = Frame(my_notebook2, width=500, height=500)

if Combohirakana:
    Combinations1 = Frame(my_notebook2, width=500, height=500)
    specialcase = Frame(my_notebook2, width=500, height=500)

if Kanji:
    radical24 = Frame(my_notebook2, width=500, height=500)
    radical48 = Frame(my_notebook2, width=500, height=500)
    radical72 = Frame(my_notebook2, width=500, height=500)
    radical96 = Frame(my_notebook2, width=500, height=500)
    radical120 = Frame(my_notebook2, width=500, height=500)
    radical144 = Frame(my_notebook2, width=500, height=500)
    radical168 = Frame(my_notebook2, width=500, height=500)
    radical192 = Frame(my_notebook2, width=500, height=500)
    radical214 = Frame(my_notebook2, width=500, height=500)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Buttons make it easier to go at a steady pace:
Startbutton = Button(HiraKana, text="Start Hiragana & Katakana", command = show).grid(column=1, row=230, sticky='S')
Stopbutton = Button(HiraKana, text="Done For Now", command = hide).grid(column=3, row=230, sticky='S')

Startbutton = Button(Dakuten, text="Start Dakuten", command = show2).grid(column=1, row=230, sticky='S')
Stopbutton = Button(Dakuten, text="Done For Now", command = hide).grid(column=3, row=230, sticky='S')

Startbutton = Button(Combohirakana, text="Start Combinations", command = show3).grid(column=1, row=230, sticky='S')
Stopbutton = Button(Combohirakana, text="Done For Now", command = hide).grid(column=3, row=230, sticky='S')

Startbutton = Button(Kanji, text="Start Radicals", command = show4).grid(column=1, row=230, sticky='S')
Stopbutton = Button(Kanji, text="Done For Now", command = hide).grid(column=3, row=230, sticky='S')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# All the text in the main tabs
myLabel = Label(HiraKana, text="What is Hiragana and Katakana?", font=("Helvetica",16))
myLabel.grid(row=0, column=0, sticky='W')

mymessage = Message(HiraKana, text="Hiragana and Katakana are Japanese syllabaries.\nEach character or kana in syllabaries has corresponding sound that is then used to spell out words phonetically.", font=("Helvetica",12), aspect=3200)
mymessage.grid(row=1, column=0, sticky='W')

myLabela = Label(HiraKana, text="\nHiragana VS. Katakana", font=("Helvetica",16))
myLabela.grid(row=3, column=0, sticky='W')

mymessagea = Message(HiraKana, text="Both Hiragana and Katakana have the exact same basic pronuncations and basic romanji, which is just the language in romanized letters. However, the situations and kana differ for each.\nHiragana is typically used for particles, prefixes, and suffixes, and words without Kanji or the where the kanji is too difficult.\nKatakana is typically used for animal names, plant names, vegetable names, onomatopoeias, company names, minerals, robotic-like speech, emphasis, and for transcribing loanwords.", font=("Helvetica",12), aspect=3200)
mymessagea.grid(row=4, column=0, sticky='W')
# Hiragana and Katakana Tab done


myLabel1 = Label(Dakuten, text="What is Dakuten?", font=("Helvetica",16))
myLabel1.grid(row=0, column=0, sticky='W')

mymessage1 = Message(Dakuten, text="Dakuten, to put it simply, modify the way the consonant is pronounced by adding a  ゛symbol after certain kana.\nThere is also another modification known as handakuten, which changes certain kana with a ゜symbol after it.", font=("Helvetica",12), aspect=3200)
mymessage1.grid(row=1, column=0, sticky='W')
# Dakuten Tab done


myLabel2 = Label(Combohirakana, text="What is Combination Hiragana and Katakana?", font=("Helvetica",16))
myLabel2.grid(row=0, column=0, sticky='W')

mymessage2 = Message(Combohirakana, text="Combination hiragana takes smaller versions of the や, ゆ, and よ kana (Example: ゃ, ゅ, and ょ) and adds them after kana that end in \"i\". The \"i\" gets dropped the consonant gets added before the \"ya\", \"yu\", and \"yo\" kana.\nCombination katakana functions in the exact same except with smaller versions of the ヤ, ユ, and ヨ kana (Example: ャ, ュ, and ョ).", font=("Helvetica",10), aspect=3200)
mymessage2.grid(row=1, column=0, sticky='W')

myLabelb = Label(Combohirakana, text="\nCombination Hiragana VS. Combination Katakana", font=("Helvetica",16))
myLabelb.grid(row=3, column=0, sticky='W')

mymessageb = Message(Combohirakana, text="Unlike combination hiragana, Combination Katakana has a special set of combination to help better fit certain loan words.\nThis special set of combinations takes smaller versions of ア, イ, ウ, エ, and オ kana (Example: ァ, ィ, ゥ, ェ, and ォ) and adds to other kana.", font=("Helvetica",10), aspect=3200)
mymessageb.grid(row=4, column=0, sticky='W')
# Combination Hiragana and Katakana Tab done


myLabel3 = Label(smalltsu, text="How Do Double Consonants and Long Vowels Work in Hiragana?", font=("Helvetica",16))
myLabel3.grid(row=0, column=0, sticky='W')

mymessage3 = Message(smalltsu, text="Double consonants in hiragana work by adding a small version of つ (Example: っ) to any of the kana besides the vowel kana.\nLong Vowels in hiragana work by adding any of the vowel kana (あ, い, う, え, and お) after other kana.\nDouble Consonant example: したい (Shitai) vs しったい (shittai)                            Long Vowel example: おばさん (obasan) vs おばあさん (obaasan)", font=("Helvetica",12), aspect=3200)
mymessage3.grid(row=1, column=0, sticky='W')

myLabelc = Label(smalltsu, text="\nHow Do Double Consonants and Long Vowels Work in Katakana?", font=("Helvetica",16))
myLabelc.grid(row=3, column=0, sticky='W')

mymessagec = Message(smalltsu, text="Double consonants in katakana work by adding a small version of ツ (Example: ッ) to any of the kana besides the vowel kana.\nLong Vowels in katakana typically work by adding a dash (ー) after any kana. In some cases it is done by adding the vowel kana (ア, イ, ウ, エ, and オ) after other kana.\nDouble Consonant example: バド (bado) vs バッド (baddo)                             Long Vowel example: テマ (tema) vs テーマ (teema)", font=("Helvetica",12), aspect=3200)
mymessagec.grid(row=4, column=0, sticky='W')

# Double Consonants and Long Vowels tab almost done


myLabel4 = Label(Kanji, text="What is Kanji?", font=("Helvetica",16))
myLabel4.grid(row=0, column=0, sticky='W')

mymessage4 = Message(Kanji, text="Kanji is derived from Ancient Chinese characters and contains over 50,000 characters, but only 2,136 Kanji are needed for basic literacy in Japanese.\nThis guide only covers radicals.", font=("Helvetica",12), aspect=3200)
mymessage4.grid(row=1, column=0, sticky='W')

myLabeld = Label(Kanji, text="\nWhat are Radicals?", font=("Helvetica",16))
myLabeld.grid(row=3, column=0, sticky='W')

mymessaged = Message(Kanji, text="Radicals are a way to classify Kanji, and are parts of kanji that can found in other kanji.\nThere are 214 radicals.", font=("Helvetica",12), aspect=3200)
mymessaged.grid(row=4, column=0, sticky='W')
# Kanji and Radical tab done
# End of text in Main Tabs
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# All of the text and images in the subtabs
myLabel5 = Message(Vowels, text="The vowels in Japanese are a, i, u, e, and o.", font=("Helvetica",14),aspect=3200)
myLabel5.grid(row=0, column=0, sticky='W')

mymessageaa = Message(Vowels, text="Hiragana:\n a➡あ  i➡い  u➡う  e➡え  o➡お\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessageaa.grid(row=1, column=0, sticky='W')

mymessageab = Message(Vowels, text="Katakana:\n a➡ア  i➡イ  u➡ウ  e➡エ  o➡オ\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessageab.grid(row=1, column=2, sticky='W')

my_img= ImageTk.PhotoImage(Image.open('images/Hiragana/Vowels.png'))
my_Label1 = Label(Vowels,image=my_img)
my_Label1.grid(row=2,column=0, sticky='w')

my_img2= ImageTk.PhotoImage(Image.open('images/Katakana/Vowels.png'))
my_Label2 = Label(Vowels,image=my_img2)
my_Label2.grid(row=2,column=2, sticky='w')
# Vowel Tab done

myLabel6 = Message(kcolumn, text="The \"K-column\" in Japanese are ka, ki, ku, ke, and ko.", font=("Helvetica",14),aspect=3200)
myLabel6.grid(row=0, column=0, sticky='W')

mymessagebb = Message(kcolumn, text="Hiragana:\n ka➡か  ki➡き  ku➡く  ke➡け  ko➡こ\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessagebb.grid(row=1, column=0, sticky='W')

mymessagebc = Message(kcolumn, text="Katakana:\n ka➡カ  ki➡キ  ku➡ク  ke➡ケ  ko➡コ\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessagebc.grid(row=1, column=2, sticky='W')

my_img3= ImageTk.PhotoImage(Image.open('images/Hiragana/K.png'))
my_Label3 = Label(kcolumn,image=my_img3)
my_Label3.grid(row=2,column=0, sticky='w')

my_img4= ImageTk.PhotoImage(Image.open('images/Katakana/K.png'))
my_Label4 = Label(kcolumn,image=my_img4)
my_Label4.grid(row=2,column=2, sticky='w')
#K Column done

myLabel7 = Message(scolumn, text="The \"S-column\" in Japanese are sa, shi, su, se, and so.", font=("Helvetica",14),aspect=3200)
myLabel7.grid(row=0, column=0, sticky='W')

mymessagebb = Message(scolumn, text="Hiragana:\n sa➡さ  shi➡し  su➡す  se➡せ  so➡そ\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessagebb.grid(row=1, column=0, sticky='W')

mymessagebc = Message(scolumn, text="Katakana:\n sa➡サ  shi➡シ  su➡ス  se➡セ  so➡ソ\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessagebc.grid(row=1, column=2, sticky='W')

my_img5= ImageTk.PhotoImage(Image.open('images/Hiragana/S.png'))
my_Label5 = Label(scolumn,image=my_img5)
my_Label5.grid(row=2,column=0, sticky='w')

my_img6= ImageTk.PhotoImage(Image.open('images/Katakana/S.png'))
my_Label6 = Label(scolumn,image=my_img6)
my_Label6.grid(row=2,column=2, sticky='w')
#S Column done

myLabel8 = Message(tcolumn, text="The \"T-column\" in Japanese are ta, chi, tsu, te, and to.", font=("Helvetica",14),aspect=3200)
myLabel8.grid(row=0, column=0, sticky='W')

mymessagecc = Message(tcolumn, text="Hiragana:\n ta➡た  chi➡ち  tsu➡つ  te➡て  to➡と\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessagecc.grid(row=1, column=0, sticky='W')

mymessagecd = Message(tcolumn, text="Katakana:\n ta➡タ  chi➡チ  tsu➡ツ  te➡テ  to➡ト\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessagecd.grid(row=1, column=2, sticky='W')

my_img7= ImageTk.PhotoImage(Image.open('images/Hiragana/T.png'))
my_Label7 = Label(tcolumn,image=my_img7)
my_Label7.grid(row=2,column=0, sticky='w')

my_img8= ImageTk.PhotoImage(Image.open('images/Katakana/T.png'))
my_Label8 = Label(tcolumn,image=my_img8)
my_Label8.grid(row=2,column=2, sticky='w')
#T Column done

myLabel9 = Message(ncolumn, text="The \"N-column\" in Japanese are na, ni, nu, ne, and no.", font=("Helvetica",14),aspect=3200)
myLabel9.grid(row=0, column=0, sticky='W')

mymessagedd = Message(ncolumn, text="Hiragana:\n na➡な  ni➡に  nu➡ぬ  ne➡ね  no➡の\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessagedd.grid(row=1, column=0, sticky='W')

mymessagede = Message(ncolumn, text="Katakana:\n na➡ナ  ni➡ニ  nu➡ヌ  ne➡ネ  no➡ノ\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessagede.grid(row=1, column=2, sticky='W')

my_img9= ImageTk.PhotoImage(Image.open('images/Hiragana/N.png'))
my_Label9 = Label(ncolumn,image=my_img9)
my_Label9.grid(row=2,column=0, sticky='w')

my_img10= ImageTk.PhotoImage(Image.open('images/Katakana/N.png'))
my_Label10 = Label(ncolumn,image=my_img10)
my_Label10.grid(row=2,column=2, sticky='w')
#N Column done

myLabel10 = Message(hcolumn, text="The \"H-column\" in Japanese are ha, hi, fu, he, and ho.", font=("Helvetica",14),aspect=3200)
myLabel10.grid(row=0, column=0, sticky='W')

mymessagee = Message(hcolumn, text="Hiragana:\n ha➡が  hi➡ひ  fu➡ふ  he➡へ  ho➡ほ\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessagee.grid(row=1, column=0, sticky='W')

mymessageef = Message(hcolumn, text="Katakana:\n ha➡ハ  hi➡ヒ  fu➡フ  he➡ヘ  ho➡ホ\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessageef.grid(row=1, column=2, sticky='W')

my_img11= ImageTk.PhotoImage(Image.open('images/Hiragana/H.png'))
my_Label11 = Label(hcolumn,image=my_img11)
my_Label11.grid(row=2,column=0, sticky='w')

my_img12= ImageTk.PhotoImage(Image.open('images/Katakana/H.png'))
my_Label12 = Label(hcolumn,image=my_img12)
my_Label12.grid(row=2,column=2, sticky='w')
#H Column done

myLabel11 = Message(mcolumn, text="The \"M-column\" in Japanese are ma, mi, mu, me, and mo.", font=("Helvetica",14),aspect=3200)
myLabel11.grid(row=0, column=0, sticky='W')

mymessageff = Message(mcolumn, text="Hiragana:\nma➡ま  mi➡み  mu➡む  me➡め  mo➡も\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessageff.grid(row=1, column=0, sticky='W')

mymessagefg = Message(mcolumn, text="Katakana:\nma➡マ  mi➡ミ  mu➡ム  me➡メ  mo➡モ\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessagefg.grid(row=1, column=2, sticky='W')

my_img13= ImageTk.PhotoImage(Image.open('images/Hiragana/M.png'))
my_Label13 = Label(mcolumn,image=my_img13)
my_Label13.grid(row=2,column=0, sticky='w')

my_img14= ImageTk.PhotoImage(Image.open('images/Katakana/M.png'))
my_Label14 = Label(mcolumn,image=my_img14)
my_Label14.grid(row=2,column=2, sticky='w')
#M Column done

myLabel12 = Message(ycolumn, text="The \"Y-column\" in Japanese are ya, yu, and yo.", font=("Helvetica",14),aspect=3200)
myLabel12.grid(row=0, column=0, sticky='W')

mymessagegg = Message(ycolumn, text="Hiragana:\nya➡や  yu➡ゆ  yo➡よ\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessagegg.grid(row=1, column=0, sticky='W')

mymessagegh = Message(ycolumn, text="Katakana:\nya➡ヤ  yu➡ユ  yo➡ヨ\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessagegh.grid(row=1, column=2, sticky='W')

my_img15= ImageTk.PhotoImage(Image.open('images/Hiragana/Y.png'))
my_Label15 = Label(ycolumn,image=my_img15)
my_Label15.grid(row=2,column=0, sticky='w')

my_img16= ImageTk.PhotoImage(Image.open('images/Katakana/Y.png'))
my_Label16 = Label(ycolumn,image=my_img16)
my_Label16.grid(row=2,column=2, sticky='w')
#Y Column done

myLabel13 = Message(rcolumn, text="The \"R-column\" in Japanese are ra, ri, ru, re, and ro.", font=("Helvetica",14),aspect=3200)
myLabel13.grid(row=0, column=0, sticky='W')

mymessagehh = Message(rcolumn, text="Hiragana:\nra➡ら  ri➡り  ru➡る  re➡れ  ro➡ろ\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessagehh.grid(row=1, column=0, sticky='W')

mymessagehi = Message(rcolumn, text="Katakana:\nra➡ラ  ri➡リ  ru➡ル  re➡レ  ro➡ロ\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessagehi.grid(row=1, column=2, sticky='W')

my_img17= ImageTk.PhotoImage(Image.open('images/Hiragana/R.png'))
my_Label17 = Label(rcolumn,image=my_img17)
my_Label17.grid(row=2,column=0, sticky='w')

my_img18= ImageTk.PhotoImage(Image.open('images/Katakana/R.png'))
my_Label18 = Label(rcolumn,image=my_img18)
my_Label18.grid(row=2,column=2, sticky='w')
#R Column done

myLabel14 = Message(wcolumn, text="The \"W-column\" in Japanese are wa and wo.\nJapanese also has single kana that is for n.", font=("Helvetica",14),aspect=3200)
myLabel14.grid(row=0, column=0, sticky='W')

mymessageii = Message(wcolumn, text="Hiragana:\nwa➡わ  wo➡を  n➡ん\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessageii.grid(row=1, column=0, sticky='W')

mymessageij = Message(wcolumn, text="Katakana:\nwa➡ワ  wo➡ヲ  n➡ン\nStroke Order:", font=("Helvetica",14), aspect=3200)
mymessageij.grid(row=1, column=2, sticky='W')

my_img19= ImageTk.PhotoImage(Image.open('images/Hiragana/W.png'))
my_Label19 = Label(wcolumn,image=my_img19)
my_Label19.grid(row=2,column=0, sticky='w')

my_img20= ImageTk.PhotoImage(Image.open('images/Katakana/W.png'))
my_Label20 = Label(wcolumn,image=my_img20)
my_Label20.grid(row=2,column=2, sticky='w')
#W Column and N done
# All subtabs in Hiragana and Katakana done!
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
myLabel15 = Message(gcolumn, text="The \"G-column\" in Japanese takes the \"K-column\" kana (か, き, く, け, こ) , and adds ゛after them to transform them into ga, gi, gu, ge, and go.", font=("Helvetica",16), aspect=3200)
myLabel15.grid(row=0, column=0, sticky='W')

mymessagejj = Message(gcolumn, text="Hiragana:\nga➡が  gi➡ぎ  gu➡ぐ  ge➡げ  go➡ご\n\n\nKatakana:\nga➡ガ  gi➡ギ  gu➡グ  ge➡ゲ  go➡ゴ", font=("Helvetica",16), aspect=3200)
mymessagejj.grid(row=1, column=0, sticky='W')

#G Column done

myLabel16 = Message(zcolumn, text="The \"Z-column\" in Japanese takes the \"S-column\" kana (さ, し, す, せ, そ), and adds ゛after them to transform them into za, ji, zu, ze, and zo.", font=("Helvetica",16), aspect=3200)
myLabel16.grid(row=0, column=0, sticky='W')

mymessagekk = Message(zcolumn, text="Hiragana:\nza➡ざ  ji➡じ  zu➡ず  ze➡ぜ  zo➡ぞ\n\n\nKatakana:\nza➡ザ  ji➡ジ  zu➡ズ  ze➡ゼ  zo➡ゾ", font=("Helvetica",16), aspect=3200)
mymessagekk.grid(row=1, column=0, sticky='W')

#Z Column done

mymessage17 = Message(dcolumn, text="The \"D-column\" in Japanese takes the \"T-column\" kana (た, ち, つ, て, と), and adds ゛after them to transform them into da, zi, zu, de, and do.\n *If typing then write zi as di and zu as du\n*Zu can sometimes be written as dzu", font=("Helvetica",16), aspect=3200)
mymessage17.grid(row=0, column=0, sticky='W')

mymessagell = Message(dcolumn, text="Hiragana:\nda➡だ zi➡ぢ  zu➡づ  de➡で  do➡ど\n\n\nKatakana:\nda➡ダ zi➡ド  zu➡ヅ  de➡デ  do➡ド", font=("Helvetica",16), aspect=3200)
mymessagell.grid(row=1, column=0, sticky='W')

#D Column done

myLabel18 = Message(bcolumn, text="The \"B-column\" in Japanese takes the \"H-column\" kana(は, ひ, ふ, へ, ほ), and adds ゛after them to transform them into ba, bi, bu, be, and bo.", font=("Helvetica",16), aspect=3200)
myLabel18.grid(row=0, column=0, sticky='W')

mymessagemm = Message(bcolumn, text="Hiragana:\nba➡ば bi➡び  bu➡ぶ  be➡べ  bo➡ぼ\n\n\nKatakana:\nba➡バ bi➡ビ  bu➡ブ  be➡ベ  bo➡ボ", font=("Helvetica",16), aspect=3200)
mymessagemm.grid(row=1, column=0, sticky='W')

#B Column done

myLabel19 = Message(pcolumn, text="The \"P-column\" in Japanese takes the \"H-column\" kana (は, ひ, ふ, へ, ほ), and adds ゜after them to transform them into pa, pi, pu, pe, and po.", font=("Helvetica",16), aspect=3200)
myLabel19.grid(row=0, column=0, sticky='W')

mymessagenn = Message(pcolumn, text="Hiragana:\npa➡ぱ pi➡ぴ  pu➡ぷ  pe➡ぺ  po➡ぽ\n\n\nKatakana:\npa➡パ pi➡ピ  pu➡プ  pe➡ペ  po➡ポ", font=("Helvetica",16), aspect=3200)
mymessagenn.grid(row=1, column=0, sticky='W')

#P Column done
# All Subtabs in Dakuten done!
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mymessage18 = Message(Combinations1, text="Basic combinations in hiragana are as follows:\n kya➡きゃ  kyu➡きゅ  kyo➡きょ\ngya➡ぎゃ  gyu➡ぎゅ  gyo➡ぎょ \nsha➡しゃ  shu➡しゅ  sho➡しょ \njya➡じゃ  jyu➡じゅ  jyo➡じょ \ncha➡ちゃ  chu➡ちゅ  cho➡ちょ \ndya➡ぢゃ  dyu➡ぢゅ  dyo➡ぢょ \nnya➡にゃ  nyu➡にゅ  nyo➡にょ \nhya➡ひゃ  hyu➡ひゅ  hyo➡ひょ \nbya➡びゃ  byu➡びゅ  byo➡びょ \npya➡ぴゃ  pyu➡ぴゅ  pyo➡ぴょ \nmya➡みゃ  myu➡みゅ  myo➡みょ \nrya➡りゃ  ryu➡りゅ  ryo➡りょ", font=("Helvetica",16), aspect=3200)
mymessage18.grid(row=0, column=0, sticky='W')

mymessage19 = Message(Combinations1, text="Basic combinations in katakana are as follows:\n kya➡キャ  kyu➡キュ  kyo➡キョ\ngya➡ギャ  gyu➡ギュ  gyo➡ギョ \nsha➡シャ  shu➡シュ  sho➡ショ \njya➡ジャ  jyu➡ジュ  jyo➡ジョ \ncha➡チャ  chu➡チュ  cho➡チョ \ndya➡ヂャ  dyu➡ヂュ  dyo➡ヂョ \nnya➡ニャ  nyu➡ニュ  nyo➡ニョ \nhya➡ヒャ  hyu➡ヒュ  hyo➡ヒョ \nbya➡ビャ  byu➡ビュ  byo➡ビョ \npya➡ピャ  pyu➡ピャ  pyo➡ピョ \nmya➡ミャ  myu➡ミュ  myo➡ミョ \nrya➡リャ  ryu➡リュ  ryo➡リョ",  font=("Helvetica",16), aspect=3200)
mymessage19.grid(row=0, column=2, sticky='W')

#Combinations done

mymessage20 = Message(specialcase, text="Special combinations in katakana are as follows:\n wi➡ウィ  we➡ウェ  wo➡ウォ\nva➡ヴァ  vi➡ヴィ  vu➡ヴ  ve➡ヴェ  vo➡ヴォ\nfa➡ファ  fi➡フィ  fe➡フェ\nshe➡シェ  je➡ジェ  che➡チェ\ntu➡トゥ  du➡ドゥ  ti/ty➡ティ  di/dy➡ディ\ntsa➡ツァ  tsi➡ツィ  tse➡ツェ  tso➡ツォ\n*vu (ヴ) is actually a special case of dakuten.", font=("Helvetica",16), aspect=3200)
mymessage20.grid(row=0, column=0, sticky='W')

#Special Combinations done
#All Subtabs in Combination Hiragana & Katakana
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
img= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 1.png'))
Label1 = Label(radical24,image=img)
Label1.grid(row=1,column=0, sticky='w')

imga= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 1-1.png'))
Label2 = Label(radical24,image=imga)
Label2.grid(row=1,column=2, sticky='w')
#end of Radical 1-24 tab

imgb= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 2.png'))
Label3 = Label(radical48,image=imgb)
Label3.grid(row=1,column=0, sticky='w')

imgc= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 2-1.png'))
Label4 = Label(radical48,image=imgc)
Label4.grid(row=1,column=2, sticky='w')
#end of Radical 25-48 tab

imgd= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 3.png'))
Label5 = Label(radical72,image=imgd)
Label5.grid(row=1,column=0, sticky='w')

imge= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 3-1.png'))
Label6 = Label(radical72,image=imge)
Label6.grid(row=1,column=2, sticky='w')
#end of Radical 49-72 tab

imgf= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 4.png'))
Label7 = Label(radical96,image=imgf)
Label7.grid(row=1,column=0, sticky='w')

imgg= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 4-1.png'))
Label8 = Label(radical96,image=imgg)
Label8.grid(row=1,column=2, sticky='w')
#end of Radical 73-96 tab

imgh= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 5.png'))
Label9 = Label(radical120,image=imgh)
Label9.grid(row=1,column=0, sticky='w')

imgi= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 5-1.png'))
Label10 = Label(radical120,image=imgi)
Label10.grid(row=1,column=2, sticky='w')
#end of Radical 97-120 tab

imgj= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 6.png'))
Label11 = Label(radical144,image=imgj)
Label11.grid(row=1,column=0, sticky='w')

imgk= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 6-1.png'))
Label12 = Label(radical144,image=imgk)
Label12.grid(row=1,column=2, sticky='w')
#end of Radical 121-144 tab

imgl= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 7.png'))
Label13 = Label(radical168,image=imgl)
Label13.grid(row=1,column=0, sticky='w')

imgm= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 7-1.png'))
Label14 = Label(radical168,image=imgm)
Label14.grid(row=1,column=2, sticky='w')
#end of Radical 145-168 tab

imgn= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 8.png'))
Label15 = Label(radical192,image=imgn)
Label15.grid(row=1,column=0, sticky='w')

imgo= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 8-1.png'))
Label16 = Label(radical192,image=imgo)
Label16.grid(row=1,column=2, sticky='w')
#end of Radical 169-192 tab

imgp= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 9.png'))
Label17 = Label(radical214,image=imgp)
Label17.grid(row=1,column=0, sticky='w')

imgq= ImageTk.PhotoImage(Image.open('images/Radicals/Kanji 9-1.png'))
Label18 = Label(radical214,image=imgq)
Label18.grid(row=1,column=2, sticky='w')
#end of Radical 193-214 tab
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#end of the subtabs!
root.mainloop()