import turtle

def main():
    count = 1
    while count <= 5:
        turtle.forward(300)
        turtle.right(144)
        count = count + 1
        print(count)
    turtle.exitonclick()

if __name__ == "__main__":
    main()
