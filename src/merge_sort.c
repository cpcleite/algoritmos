void main()
{
    char c1[4] = "acxz";
    char c2[5] = "bdsty";
    int a, b;

    a = tamanho(c1);
    b = tamanho(c2);
}

int tamanho(char *ptr)
{
    int len = 0;
    while (ptr != "\0")
    {

        len++;
    }
    return len;
}
