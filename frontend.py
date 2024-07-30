import tkinter as tk
import joblib
import numpy as np

my_model = joblib.load("sallery_predictor.joblib")

def predcitsallry():
    exp = float(ent.get())
    exp = np.array(exp)
    reshaped_Data = exp.reshape(-1, 1)
    
    sallery = my_model.predict(reshaped_Data)[0]
    # print(sallery)

    lblshow.config(text = f"Your predicted Sallery is : {str(sallery)[:7]}")

    ent.delete(0, tk.END)

app = tk.Tk()
app.geometry("700x300")
app.config(background="#9ff78f")
app.title("Sallery Predictor")

lbl = tk.Label(app, text = "Sallery Predictor", font=("robort", 32, "bold"), bg = "#9ff78f", fg = "green")
lbl.pack(pady=14)

ent = tk.Entry(app, font=("robort", 27))
ent.pack()

btn = tk.Button(app, text = "Predict", bg = "green", fg = "#9ff78f", font = ("robort", 20, "bold"), command = predcitsallry)
btn.pack(pady=14)

lblshow = tk.Label(app, text = "", font=("robort", 18), bg = "#9ff78f", fg = "green")
lblshow.pack()


app.mainloop()