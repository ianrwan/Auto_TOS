class Test
{
    private List<int> myList = new List<int>();
    public List<int> MyList
    {
        get
        {
            return myList;
        }
    }

    public Test(int counter)
    {
        myList.Add(counter);
    }
}

class Program
{
    public static void Main(string[] args)
    {
        for(int i = 0 ; i < 5 ; i++)
        {
            Test test = new Test(i);
            foreach(int data in test.MyList)
            {
                Console.Write(data+" ");
            }
            Console.WriteLine();
        }
    }
}
