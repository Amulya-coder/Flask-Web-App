from website import create_app

app = create_app()

#only when we run this not we import
if __name__ == "__main__":
    #this will run our flask application 
    app.run(debug=True)

 #(debug==True) means when we change something in the code then our server automatically
 #  restart again 