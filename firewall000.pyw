from tkinter import messagebox  
import shutil, os, re
import tkinter as tk

#-----------------------------------#
# [PGX] - NINGUN SISTEMA ES SEGURO  #
#-----------------------------------#

def host_del():
 software=os.name
 if software == 'nt':
  os.system(f"@echo off>{ruta}")
 else:
  os.system(f">{ruta}")

ruta='C:\\Windows\\System32\\drivers\\etc\\hosts'
hostname='127.0.0.1'

def restricted_url():
 url = entry_clave.get()
 with open(ruta, "a") as f:
  f.write(f"\n{hostname}\t {url}")
 messagebox.showwarning("ADVERTENCIA", "SE DENEGO EL DOMINIO")

def restricted_dic_domains():
 with open('dominios.txt', 'r') as f:
  x=f.readlines()
  for i in x:
   domain=i.replace("\n", "")
   with open(ruta, "a") as f:
    f.write(f"\n{hostname}\t www.{domain}")
    f.close()
 messagebox.showwarning("ADVERTENCIA", "SE HAN PROHIBIDO ACCEDER TODOS LOS DOMINIOS DEL DICCIONARIO")

def all_delete():
 file_host=[]
 with open(ruta, 'r') as f:
  v = f.readlines()
  for i in v:
   r=i.replace("\n", "")
   if r:
    lineas=r[0]
    if lineas == '#':
     file_host.append(r)
 
 host_del()
 for i in file_host:
  with open(ruta, 'a') as f:
   f.write(f"{i}\n")
   f.close()
 messagebox.showinfo("Operacion exitosa", "SIN RESTRCCIONES")

def eliminar_url():
 url = entry_clave2.get()
 nw=[]
 with open(ruta, 'r') as f:
  v = f.readlines()
  for i in v:
   r=i.replace("\n", "")
   if r:
    buscar=re.search(url, r, re.IGNORECASE)
    if buscar == None:
     nw.append(r)
 host_del()
 for d in nw:
  with open(ruta, 'a') as f:
   f.write(f"{d}\n")
   f.close()
 messagebox.showinfo("Operacion exitosa", "DOMINIO SIN RESTRCCION")
def url_list():
 nueva_ventana = tk.Toplevel(root)
 nueva_ventana.title("Listado de Dominios Bloqueados")
 texto = tk.Text(nueva_ventana, wrap=tk.WORD, height=20, width=50)
 texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
 scrollbar = tk.Scrollbar(nueva_ventana, command=texto.yview)
 scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
 with open(ruta, 'r') as f:
  v = f.readlines()
  for i in v:
   r=i.replace("\n", "")
   if r:
    lineas=r[0]
    if lineas != '#':
     rr=f"  {r.split()[-1]}"
     texto.insert(tk.END, rr + "\n")

def input1():
 input_frame.pack(pady=(10, 20))

def input2():
 input_frame2.pack(pady=(10, 20))

root=tk.Tk()
root.configure(bg="black")
root.title("INTERFAZ GRAFICA")
root.geometry("600x700")
input_frame = tk.Frame(root, bg="black")
label_clave = tk.Label(input_frame, text="DOMINIO: ", bg="black", fg="white")
label_clave.pack(side=tk.LEFT, padx=5)
entry_clave = tk.Entry(input_frame)
entry_clave.pack(side=tk.LEFT)
button_guardar = tk.Button(input_frame, text="PROHIBIR", command=restricted_url)
button_guardar.pack(side=tk.LEFT)
input_frame2 = tk.Frame(root, bg="black")
label_clave2 = tk.Label(input_frame2, text="DOMINIO:", bg="black", fg="white")
label_clave2.pack(side=tk.LEFT, padx=5)
entry_clave2 = tk.Entry(input_frame2)
entry_clave2.pack(side=tk.LEFT)
button_guardar2 = tk.Button(input_frame2, text="PERMITIR", command=eliminar_url)
button_guardar2.pack(side=tk.LEFT)
denied_all = tk.Button(root, text="Denegar acceso a dominios del diccionario", command=restricted_dic_domains, width=37, bg="blue", fg="white", font=("Calibri", 10, "bold"))
denied_all.pack(pady=(50, 20))
restricted_url = tk.Button(root, text="Denegar acceso a un dominio", command=input1, width=37)
restricted_url.pack(pady=(5, 20))
all_delete = tk.Button(root, text="Permitir acceso a todos los dominios", command=all_delete, width=37, bg="blue", fg="white", font=("Calibri", 10, "bold"))
all_delete.pack(pady=(5, 20))
eliminar_url = tk.Button(root, text="Permitir acceso a un dominio", command=input2, width=37)
eliminar_url.pack(pady=(5, 20))
listar_button = tk.Button(root, text="Listar todos los dominios bloqueados", command=url_list, width=37, bg="blue", fg="white", font=("Calibri", 10, "bold"))
listar_button.pack(pady=(5, 20))
root.mainloop()
