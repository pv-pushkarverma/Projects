#include<iostream>
#include<ctime>
#include<cstdlib>
#include<unistd.h>
using namespace std;

void generate_matrix(int arr[][4])
{
    int num[15]={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
    srand(time(NULL));
    int index=15;

    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(i==3 && j==3)
                break;

            int random=rand()%index;
            arr[i][j]=num[random];
            num[random]=num[index-1];
            index--;
        }
    }
    arr[3][3]=0;
}

void print_matrix(int mat[4][4])
{
    cout<<"________________________"<<endl;
    for(int i=0;i<4;i++)
    {
        cout<<"|";
        for(int j=0;j<4;j++)
        {
            if(mat[i][j]==0)
                cout<<"    | ";
            else if(mat[i][j]<10)
                cout<<"  "<<mat[i][j]<<" | ";
            else
                cout<<" "<<mat[i][j]<<" | ";
        }
        cout<<endl;
    }
    cout<<"------------------------"<<endl;
    cout<<"\033[1;35m";
}

int get_key()
{
    char a = getchar();
    if(a=='e' || a=='E')
        return -1;
    if (a != '\x1b')
        return 0;

    char b = getchar();
    char c = getchar();

    if (b == '[' && c >= 'A' && c <= 'D') {
        switch (c) {
            case 'A':
                return 1; // Up arrow key
            case 'B':
                return 2; // Down arrow key
            case 'C':
                return 3; // Right arrow key
            case 'D':
                return 4; // Left arrow key
        }
    }
    return 0;
}

void swap_num(int &a,int &b)
{
    int temp=a;
    a=b;
    b=temp;
}

int shift_up(int mat[4][4])
{
    int i,j;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(mat[i][j]==0)
                break;
        }
        if(j==4)
            j=0;
        if(mat[i][j]==0)
                break;
    }

    if(i>0)
    {
        swap_num(mat[i][j],mat[i-1][j]);
        return 1;
    }
    else
        return 0;
}

int shift_down(int mat[4][4])
{
    int i,j;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(mat[i][j]==0)
                break;
        }
        if(mat[i][j]==0)
                break;
    }

    if(i<3)
    {
        swap_num(mat[i][j],mat[i+1][j]);
        return 1;
    }
    else
        return 0;
}

int shift_right(int mat[4][4])
{
    int i,j;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(mat[i][j]==0)
                break;
        }
        if (j==4)
            j=0;
        if(mat[i][j]==0)
                break;
    }

    if(j<3)
    {
        swap_num(mat[i][j],mat[i][j+1]);
        return 1;
    }
    else
        return 0;
}

int shift_left(int mat[4][4])
{
    int i,j;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(mat[i][j]==0)
                break;
        }
        if(j==4) //if next row first element has 0 then it considers,
            j=0; //j==4 as next element and swaps it with previous so we reset,j to 0 to avoid it
        if(mat[i][j]==0)
                break;
    }

    if(j>0)
    {
        swap_num(mat[i][j],mat[i][j-1]);
        return 1;
    }
    else
        return 0;
}

int check_win(int mat[4][4])
{
    int value=1;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++,value++)
        {
            if(i==3 && j==3)
                break;
            if(mat[i][j]!=value)
                return 0;
        }
    }
    return 1;
}

void rules()
{
    cout<<"\033[1;35m";
    cout<<endl<<"Welcome to Number Shifting Game"<<endl<<endl<<endl;
    cout<<"\033[1;36m";
    cout<<"1. Press arrow keys to move."<<endl;
    cout<<"   Move Up : Press Up Arrow Key"<<endl;
    cout<<"   Move Down : Press Down Arrow Key"<<endl;
    cout<<"   Move Right : Press Right Arrow Key"<<endl;
    cout<<"   Move Left : Press Left Arrow Key"<<endl;
    cout<<endl<<endl<<"2. There are limited number of moves"<<endl;
    cout<<endl<<endl<<"3. Winning Situation "<<endl;
    cout<<"\033[1;32m";
    int mat[4][4]={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
    print_matrix(mat);
    cout<<"\033[1;36m";
    cout<<endl<<"4.Press E or e to exit."<<endl;
    cout<<"\033[1;33m";
    cout<<endl<<endl<<"Good Luck!"<<endl;
    cout<<"\033[1;0m";
}

int main()
{   
    int matrix[4][4];
    int moves=100;
    generate_matrix(matrix);
    
    rules();
    cout<<endl;

    string name;
    cout<<"\033[1;32m";
    cout<<endl<<"Enter your name : ";
    cin>>name;
    system("clear");
    while (cin.get() != '\n');//clear input buffer
    
    while(moves)
    {
        if(check_win(matrix))
        {
            cout<<"\033[1;33m";
            cout<<"Congratulations !!! "<<name<<" you win in "<<100-moves<<" moves."<<endl;
            return 0;
        }

        cout<<"\033[1;33m"<<"Player : "<<"\033[1;32m"<<name<<endl;
        cout<<"\033[1;33m"<<"Moves  : "<<"\033[1;32m"<<moves<<endl<<endl;

        cout<<"\033[1;34m";
        print_matrix(matrix);
        cout<<endl<<endl;

        int key=get_key();
        
        while (cin.get() != '\n'); // to clear newline character enter key

        switch(key)
        {
            case -1:
            {
                cout<<"Quitting Game."<<endl;
                exit(0);
            }
            case 0:
            {
                cout<<"Enter valid arrow key "<<endl;
                getchar();
                break;
            }
            case 1: // UP
            {
                if(shift_up(matrix))
                    moves--;
                print_matrix(matrix);
                break;
            }
            case 2: // DOWN
            {
                if(shift_down(matrix))
                    moves--;
                print_matrix(matrix);
                break;
            }
            case 3: // RIGHT
            {
                if(shift_right(matrix))
                    moves--;
                print_matrix(matrix);
                break;
            }
            case 4: // LEFT
            {
                if(shift_left(matrix))
                    moves--;
                print_matrix(matrix);
                break;
            }
        }
        system("clear");
    }

    if(!moves)
        cout<<"\033[1;31m"<<"Moves Finished !\nYou Lost !!!"<<endl;   
}