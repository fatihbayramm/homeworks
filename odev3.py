import psycopg2
conn = psycopg2.connect("dbname=odevler user=postgres")
cur = conn.cursor()
cur.execute("SELECT * FROM students;")
records = cur.fetchall()

print("-"*30)

veri = input("""Öğrenci bilgi sistemine hoşgeldiniz . 
            (1)--> Öğrencileri Listele .
            (2)--> Öğrenci ekle .
            (3)--> Öğrenci silme .
            """)
print("-"*30)

if veri == "1":
    cur.execute("SELECT * FROM students ;")
    records = cur.fetchall()
    print(records)
    
elif veri == "2":
    idd = int(input("id : "))
    ad = input("Ad : ")
    soyad = input("Soyad : ") 
    numara = int(input("Numara : "))
    cur.execute(f"""INSERT INTO students (id, name, lastname, number)
                values({idd}, '{ad}', '{soyad}', {numara});""")
    conn.commit()            
    print(f"{ad} {soyad}, {numara} numarasıyla sisteme başarıyla eklenmiştir !")             
elif veri == "3":
    numara2 = int(input("Öğrencinin numarası --> "))
    result = cur.execute(f"DELETE FROM students WHERE number = {numara2};")
    conn.commit()
    print(f"{numara2} numaralı öğrenci başarıyla listeden silindi . ")  












        
        
        
        

  

        



