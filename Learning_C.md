Initialize and assign a value to an integer, float, and char variable. Then print each one with a sentence on a new line describing variable data type.

```c

#include <stdio.h>

int main(void)
{
  int integer = 5;
  float floatvar = 3.14;
  char string[] = "Hello, World!";

  printf("%d is an integer!\n", integer);
  printf("%f is a float!\n", floatvar);
  printf("%s is a char!\n", string);

}
```

### Assignment - 3

Prompt the user to input their first and last name and then print 
them a welcome message. Try storing the input as a char variable's 
value.

Easy Mode: Allocate an arbitrary amount of indices to your char array and pray to the gods that the user input fits.

Extra Credit: Dynamically allocate the array size of your char variable based on the length of the user's input.

```c
#include <stdio.h>

int main(void)
{
    //initialize vars
    char a[10],b[10];

    //prompt user to input first and last name and use scanf() to store those to the initiliazed vars
    printf("Enter Your First Name: ");
    scanf("%s",&a);
    printf("Enter Your Last Name: ");
    scanf("%s",&b);

    //print the welcome message!
    printf("Hello %s %s !\n",a,b);
}
```

### assignment - 4

Prompt the user to input the length of a radius and then print the area of the user's circle to the terminal.
Extra credit: Use the #define feature of C to assign the value 3.14 to PIE.

```c
#include <stdio.h>
//define a value for PIE
#define PIE 3.14

int main(void)
{
  //initialize variable
  float radius;

  //get user input and store it
  printf("Enter the radius of your circle: ");
  scanf("%f", &radius);

  //do the maths
  float area;
  area = PIE * (radius * radius);

  printf("The area of your circle is %f", area);
}
```

###  assignment - 5
Prompt the user for a number of seconds. Take the user's input and convert the number of seconds into its duration in Hours, Minutes, and remaining Seconds.
Extra Credit: Make sure the Hours, Minutes, and Seconds print with no decimal places.

```c
#include <stdio.h>

int main(void){
    // initillize variables
    int hours,minutes,secounds,n,a;
    printf("Enter the amount of seconds: ");
    scanf("%d",&n);
    a = n;
    // Maths
    n = n % (24 * 3600);
    hours = n / 3600;

    n %= 3600;
    minutes = n / 60;

    n %= 60;
    secounds = n;
    printf("%d seconds is equal to %d hours, %d minutes, and %d seconds.#",a,hours,minutes,secounds);
}
```
