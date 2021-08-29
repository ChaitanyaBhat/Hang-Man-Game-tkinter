import tkinter as tk

w=0     
    
def pick_word():
    global new_s,count,life,typed_ch,w,word
    count=0;life=7;typed_ch=[];new_s=''	
    word_list=['drawing','connection','library','trecking','internet','valuation','journey','nature','music','picture']
    word=word_list[w]
    for letter in word:
        new_s+='_'
    # print(new_s)
    label_announce.config(text="Guess the word:")
    label_spaces.config(text=new_s)
    label_enterCh.config(text="Enter a character:")
    label_char.config(text="")
    label_result.config(text="")

def guess_word():
    global w,word,count,life,typed_ch,new_s
    # print(new_s,word)
    ch=char_entry.get()  
    k=0;new=''
    if count<len(word):
        if ch in word and ch not in typed_ch:
            # print(k,ch,count,life)
            while k<len(word):	
                if ch==word[k]:
                    count+=1
                    new+=ch
                    if count==len(word):
                        result="You Win"  # ask="Do you want to continue?"
                        w+=1
                    else:
                        result="Right guess"
                elif new_s[k]==word[k]:
                    new+=new_s[k]			
                else:
                    new+='_'
                k+=1
            new_s=new		
        else:
            result="Wrong Guess"
            life-=1
            if life==0:
                result="You Lose" # ask="Do you want to continue?"
                w+=1
        typed_ch+=ch
    label_char.config(text=new_s)
    label_result.config(text=result)

root=tk.Tk()
root.title("Hang Man Game")
root.minsize(800,500)
label_spaces=tk.Label(root,text="")
label_announce=tk.Label(root,text="")
label_enterCh=tk.Label(root,text="")
label_char=tk.Label(root,text="")
label_result=tk.Label(root,text="")
char_entry=tk.Entry(root)
start_button=tk.Button(root,bg="orange",fg="white",text="Start")
submit_button=tk.Button(root,bg="red",fg="white",text="Submit")

label_spaces.grid(row=0,column=1)
label_announce.grid(row=0,column=0)
label_enterCh.grid(row=1,column=0)
char_entry.grid(row=1,column=1)
label_char.grid(row=2,column=1)
label_result.grid(row=2,column=0)
start_button.grid(row=3,column=1)
submit_button.grid(row=4,column=0)

start_button.config(command=pick_word)
submit_button.config(command=guess_word)

root.mainloop()

				
