#include <iostream>
#include <string>
#include <string.h>
#include <cmath>
#include <fstream>
#include <stack>
#include <ctime>
#include <cstdlib>
#include <queue>
using namespace std;
const int N = 100000;
const int M = 100;

//Узел дерева можно описать как структуру :

struct BSTnode {
    int key;           // поле данных
    struct BSTnode* left;  // левый потомок
    struct BSTnode* right; // правый потомок
};

//префиксный вид
void treeprintpref(BSTnode* tree) {
    if (tree != NULL) { //Пока не встретится пустой узел
        cout << tree->key << " "; //Отображаем корень дерева
        treeprintpref(tree->left); //Рекурсивная функция для левого поддерева
        treeprintpref(tree->right); //Рекурсивная функция для правого поддерева
    }
}

//инфиксный вид
void treeprintinf(BSTnode* tree) {
    if (tree != NULL) { //Пока не встретится пустой узел
        treeprintinf(tree->left); //Рекурсивная функция для левого поддерева
        cout << tree->key << " "; //Отображаем корень дерева
        treeprintinf(tree->right); //Рекурсивная функция для правого поддерева
    }
}

//постфиксный вид
void treeprintpost(BSTnode* tree) {
    if (tree != NULL) { //Пока не встретится пустой узел
        treeprintpost(tree->left); //Рекурсивная функция для левого поддерева
        treeprintpost(tree->right); //Рекурсивная функция для правого поддерева
        cout << tree->key << " "; //Отображаем корень дерева
    }
}

//Добавление узлов в дерево
struct BSTnode* addnode(int x, BSTnode* tree) {
    if (tree == NULL) { // Если дерева нет, то формируем корень
        tree = new BSTnode; // память под узел
        tree->key = x;   // поле данных
        tree->left = NULL;
        tree->right = NULL; // ветви инициализируем пустотой
    }
    else  if (x < tree->key)   // условие добавление левого потомка
        tree->left = addnode(x, tree->left);
    else    // условие добавление правого потомка
        tree->right = addnode(x, tree->right);
    return(tree);
}
//Удаление поддерева
void DeleteTree(BSTnode* tree) {
    if (tree != NULL) {
        DeleteTree(tree->left);
        DeleteTree(tree->right);
        delete tree;
    }
}
BSTnode* MinValue(BSTnode* Tree)
{
    if (Tree->left != NULL) {
        return MinValue(Tree->left);
    }
    else {
        cout << Tree->key;
    }
}

BSTnode* findmin(BSTnode* node) // поиск узла с минимальным ключом в дереве p 
{
    return node->left ? findmin(node->left) : node;
}
//Так как в бинарном дереве поиска для каждого узла справедливо, что left < right, 
//то соответственно для нахождения наибольшего элемента 
//надо топать от корня по правым веткам до упора - там и будет наибольший.
BSTnode* MaxValue(BSTnode* Tree)
{
    if (Tree->right != NULL) {
        return  MaxValue(Tree->right);
    }
    else 
    {
        cout << Tree->key;
    }
}
int NumberOfNodes(BSTnode* Tree) 
{
    if (Tree == NULL) return 0;
    return NumberOfNodes(Tree->left) + 1 + NumberOfNodes(Tree->right);
}
//Высота(максимальная глубина) дерева определяется количеством уровней, 
//на которых располагаются его вершины.
//Высота пустого дерева равна нулю, высота дерева из одного корня – единице.
//На первом уровне дерева может быть только одна вершина – корень дерева, 
//на втором – потомки корня дерева, на третьем – потомки потомков корня дерева и т.д.
int HeightBTree(BSTnode* Tree) 
{
    int x = 0, y = 0;
    if (Tree == NULL) return 0;     //пустое дерево или дошли до листа
    if (Tree->left) x = HeightBTree(Tree->left); //высота левого поддерева
    if (Tree->right) y = HeightBTree(Tree->right);  //высота правого поддерева
    if (x > y) return x + 1;    //+1 от корня к левому поддереву
    else return y + 1;   //+1 от корня к правому поддереву
}
//поиск элемента в бинарном дереве поиска
BSTnode* Search(BSTnode* Tree, int x) 
{
    if (Tree == NULL) return NULL;
    if (Tree->key == x) return Tree;
    if (x < Tree->key) return Search(Tree->left, x);
    else
        return Search(Tree->right, x);
}
BSTnode* DeleteNode(BSTnode* node, int x) {
    if (node == NULL)
        return node;

    if (x == node->key) {

        BSTnode* help1;
        if (node->right == NULL)
            help1 = node->left;
        else {

            BSTnode* help2 = node->right;
            if (help2->left == NULL) {
                help2->left = node->left;
                help1 = help2;
            }
            else {

                BSTnode* pmin = help2->left;
                while (pmin->left != NULL) {
                    help2 = pmin;
                    pmin = help2->left;
                }
                help2->left = pmin->right;
                pmin->left = node->left;
                pmin->right = node->right;
                help1 = pmin;
            }
        }
        delete node;
        return help1;
    }
    else if (x < node->key)
        node->left = DeleteNode(node->left, x);
    else
        node->right = DeleteNode(node->right, x);
    return node;
}

//=================================================================================

class RBtree {
    struct node_st { node_st* p1, * p2; int value; bool red; }; // структура узла
    node_st* tree_root;                 //!< корень
    int nodes_count;                    //!< число узлов дерева
private:
    node_st* NewNode(int value);        //!< выделение новой вешины
    void DelNode(node_st*);             //!< удаление вершины
    void Clear(node_st*);               //!< снос дерева (рекурсивная часть)
    node_st* Rotate21(node_st*);        //!< вращение влево
    node_st* Rotate12(node_st*);        //!< вращение вправо
    void BalanceInsert(node_st**);      //!< балансировка вставки
    bool BalanceRemove1(node_st**);     //!< левая балансировка удаления
    bool BalanceRemove2(node_st**);     //!< правая балансировка удаления
    bool Insert(int, node_st**);         //!< рекурсивная часть вставки
    bool GetMin(node_st**, node_st**);   //!< найти и убрать максимальный узел поддерева
    bool Remove(node_st**, int);         //!< рекурсивная часть удаления
public: // отладочная часть
    enum check_code { error_balance, error_struct, ok }; // код ошибки
    void Show();                        //!< вывод дерева
    check_code Check();                 //!< проверка дерева
    bool TreeWalk(bool*, int);           //!< обход дерева и сверка значений с массивом
private: // отладочная часть
    void Show(node_st*, int, char);       //!< вывод дерева, рекурсивная часть
    check_code Check(node_st*, int, int&);//!< проверка дерева (рекурсивная часть)
    bool TreeWalk(node_st*, bool*, int);  //!< обход дерева и сверка значений с массивом (рекурсивная часть)
public:
    RBtree();
    ~RBtree();
    void Clear();           //!< снести дерево              
    bool Find(int);         //!< найти значение
    void Insert(int);       //!< вставить значение
    void Remove(int);       //!< удалить значение
    int GetNodesCount();    //!< узнать число узлов
};


RBtree::RBtree()
{
    tree_root = 0;
    nodes_count = 0;
}

RBtree::~RBtree()
{
    Clear(tree_root);
}

int RBtree::GetNodesCount()
{
    return nodes_count;
}

// выделение новой вешины
RBtree::node_st* RBtree::NewNode(int value)
{
    nodes_count++;
    node_st* node = new node_st;
    node->value = value;
    node->p1 = node->p2 = 0;
    node->red = true;
    return node;
}

// удаление вершины
void RBtree::DelNode(node_st* node)
{
    nodes_count--;
    delete node;
}

// снос дерева (рекурсивная часть)
void RBtree::Clear(node_st* node)
{
    if (!node) return;
    Clear(node->p1);
    Clear(node->p2);
    DelNode(node);
}

// вывод дерева, рекурсивная часть
//! \param node узел
//! \param depth глубина
//! \param dir   значёк
//! \code Show(root,0,'*'); \endcode
void RBtree::Show(node_st* node, int depth, char dir)
{
    int n;
    if (!node) return;
    for (n = 0; n < depth; n++) putchar(' ');
    printf("%c[%d] (%s)\n", dir, node->value, node->red ? "red" : "black");
    Show(node->p1, depth + 2, '-');
    Show(node->p2, depth + 2, '+');
}


// вращение влево
//! \param index индеск вершины
//! \result новая вершина дерева
RBtree::node_st* RBtree::Rotate21(node_st* node)
{
    node_st* p2 = node->p2;
    node_st* p21 = p2->p1;
    p2->p1 = node;
    node->p2 = p21;
    return p2;
}

// вращение вправо
//! \param index индеск вершины
//! \result новая вершина дерева
RBtree::node_st* RBtree::Rotate12(node_st* node)
{
    node_st* p1 = node->p1;
    node_st* p12 = p1->p2;
    p1->p2 = node;
    node->p1 = p12;
    return p1;
}


// балансировка вершины
void RBtree::BalanceInsert(node_st** root)
{
    node_st* p1, * p2, * px1, * px2;
    node_st* node = *root;
    if (node->red) return;
    p1 = node->p1;
    p2 = node->p2;
    if (p1 && p1->red) {
        px2 = p1->p2;             // задача найти две рядом стоящие крастне вершины
        if (px2 && px2->red) p1 = node->p1 = Rotate21(p1);
        px1 = p1->p1;
        if (px1 && px1->red) {
            node->red = true;
            p1->red = false;
            if (p2 && p2->red) { // отделаемся перекраской вершин
                px1->red = true;
                p2->red = false;
                return;
            }
            *root = Rotate12(node);
            return;
        }
    }
    // тоже самое в другую сторону
    if (p2 && p2->red) {
        px1 = p2->p1;             // задача найти две рядом стоящие крастне вершины
        if (px1 && px1->red) p2 = node->p2 = Rotate12(p2);
        px2 = p2->p2;
        if (px2 && px2->red) {
            node->red = true;
            p2->red = false;
            if (p1 && p1->red) { // отделаемся перекраской вершин
                px2->red = true;
                p1->red = false;
                return;
            }
            *root = Rotate21(node);
            return;
        }
    }
}


bool RBtree::BalanceRemove1(node_st** root)
{
    node_st* node = *root;
    node_st* p1 = node->p1;
    node_st* p2 = node->p2;
    if (p1 && p1->red) {
        p1->red = false; return false;
    }
    if (p2 && p2->red) { // случай 1
        node->red = true;
        p2->red = false;
        node = *root = Rotate21(node);
        if (BalanceRemove1(&node->p1)) node->p1->red = false;
        return false;
    }
    unsigned int mask = 0;
    node_st* p21 = p2->p1;
    node_st* p22 = p2->p2;
    if (p21 && p21->red) mask |= 1;
    if (p22 && p22->red) mask |= 2;
    switch (mask)
    {
    case 0:     // случай 2 - if((!p21 || !p21->red) && (!p22 || !p22->red))
        p2->red = true;
        return true;
    case 1:
    case 3:     // случай 3 - if(p21 && p21->red)
        p2->red = true;
        p21->red = false;
        p2 = node->p2 = Rotate12(p2);
        p22 = p2->p2;
    case 2:     // случай 4 - if(p22 && p22->red)
        p2->red = node->red;
        p22->red = node->red = false;
        *root = Rotate21(node);
    }
    return false;
}

bool RBtree::BalanceRemove2(node_st** root)
{
    node_st* node = *root;
    node_st* p1 = node->p1;
    node_st* p2 = node->p2;
    if (p2 && p2->red) { p2->red = false; return false; }
    if (p1 && p1->red) { // случай 1
        node->red = true;
        p1->red = false;
        node = *root = Rotate12(node);
        if (BalanceRemove2(&node->p2)) node->p2->red = false;
        return false;
    }
    unsigned int mask = 0;
    node_st* p11 = p1->p1;
    node_st* p12 = p1->p2;
    if (p11 && p11->red) mask |= 1;
    if (p12 && p12->red) mask |= 2;
    switch (mask) {
    case 0:     // случай 2 - if((!p12 || !p12->red) && (!p11 || !p11->red))
        p1->red = true;
        return true;
    case 2:
    case 3:     // случай 3 - if(p12 && p12->red)
        p1->red = true;
        p12->red = false;
        p1 = node->p1 = Rotate21(p1);
        p11 = p1->p1;
    case 1:     // случай 4 - if(p11 && p11->red)
        p1->red = node->red;
        p11->red = node->red = false;
        *root = Rotate12(node);
    }
    return false;
}


bool RBtree::Find(int value)
{
    node_st* node = tree_root;
    while (node) {
        if (node->value == value) return true;
        node = node->value > value ? node->p1 : node->p2;
    }
    return false;
}


// рекурсивная часть вставки
//! \result true если изменений небыло или балансировка в данной вершине не нужна
bool RBtree::Insert(int value, node_st** root)
{
    node_st* node = *root;
    if (!node) *root = NewNode(value);
    else {
        if (value == node->value) return true;
        if (Insert(value, value < node->value ? &node->p1 : &node->p2)) return true;
        BalanceInsert(root);
    }
    return false;
}


// найти и убрать максимальный узел поддерева
//! \param root корень дерева в котором надо найти элемент
//! \retval res эелемент который был удалён
//! \result true если нужен баланс
bool RBtree::GetMin(node_st** root, node_st** res)
{
    node_st* node = *root;
    if (node->p1) {
        if (GetMin(&node->p1, res)) return BalanceRemove1(root);
    }
    else {
        *root = node->p2;
        *res = node;
        return !node->red;
    }
    return false;
}


// рекурсивная часть удаления
//! \result true если нужен баланс
bool RBtree::Remove(node_st** root, int value)
{
    node_st* t, * node = *root;
    if (!node) return false;
    if (node->value < value) {
        if (Remove(&node->p2, value)) return BalanceRemove2(root);
    }
    else if (node->value > value) {
        if (Remove(&node->p1, value)) return BalanceRemove1(root);
    }
    else {
        bool res;
        if (!node->p2) {
            *root = node->p1;
            res = !node->red;
        }
        else {
            res = GetMin(&node->p2, root);
            t = *root;
            t->red = node->red;
            t->p1 = node->p1;
            t->p2 = node->p2;
            if (res) res = BalanceRemove2(root);
        }
        DelNode(node);
        return res;
    }
    return 0;
}


// вывод дерева
void RBtree::Show()
{
    printf("[tree]\n");
    Show(tree_root, 0, '*');
}

// функция вставки
void RBtree::Insert(int value)
{
    Insert(value, &tree_root);
    if (tree_root) tree_root->red = false;
}

// удаление узла
void RBtree::Remove(int value)
{
    Remove(&tree_root, value);
}

// снос дерева
void RBtree::Clear()
{
    Clear(tree_root);
    tree_root = 0;
}


// проверка дерева (рекурсивная часть)
//! \param tree дерево
//! \param d    текущая чёрная глубина
//! \param h    эталонная чёрная глубина
//! \result 0 или код ошибки
RBtree::check_code RBtree::Check(node_st* tree, int d, int& h)
{
    if (!tree) {
        // количество чёрных вершин на любом пути одинаковое
        if (h < 0) h = d;
        return h == d ? ok : error_balance;
    }
    node_st* p1 = tree->p1;
    node_st* p2 = tree->p2;
    // красная вершина должна иметь чёрных потомков
    if (tree->red && (p1 && p1->red || p2 && p2->red)) return error_struct;
    if (p1 && tree->value<p1->value || p2 && tree->value>p2->value) return error_struct;
    if (!tree->red) d++;
    check_code n = Check(p1, d, h); if (n) return n;
    return Check(p2, d, h);
}


// проверка дерева
RBtree::check_code RBtree::Check()
{
    int d = 0;
    int h = -1;
    if (!tree_root) return ok;
    if (tree_root->red) return error_struct;
    return Check(tree_root, d, h);
}

// обход дерева и сверка значений с массивом (рекурсивная часть)
//! \param node  корень дерева
//! \param array массив для сверки
//! \param size  размер массива
bool RBtree::TreeWalk(node_st* node, bool* array, int size)
{
    if (!node) return false;
    int value = node->value;
    if (value < 0 || value >= size || !array[value]) return true;
    array[value] = false;
    return TreeWalk(node->p1, array, size) || TreeWalk(node->p2, array, size);
}

// обход дерева и сверка значений с массивом
//! \param array массив для сверки
//! \param size  размер массива
bool RBtree::TreeWalk(bool* array, int size)
{
    if (TreeWalk(tree_root, array, size)) return true;
    for (int n = 0; n < size; n++) if (array[n]) return true;
    return false;
}


//================================================================

struct nodeavl // структура для представления узлов дерева
{
    int key;
    unsigned char height;
    nodeavl* left;
    nodeavl* right;
    nodeavl(int k) { key = k; left = right = 0; height = 1; }
};

unsigned char height(nodeavl* p)
{
    return p ? p->height : 0;
}

int bfactor(nodeavl* p)
{
    return height(p->right) - height(p->left);
}

void fixheight(nodeavl* p)
{
    unsigned char hl = height(p->left);
    unsigned char hr = height(p->right);
    p->height = (hl > hr ? hl : hr) + 1;
}

nodeavl* rotateright(nodeavl* p) // правый поворот вокруг p
{
    nodeavl* q = p->left;
    p->left = q->right;
    q->right = p;
    fixheight(p);
    fixheight(q);
    return q;
}

nodeavl* rotateleft(nodeavl* q) // левый поворот вокруг q
{
    nodeavl* p = q->right;
    q->right = p->left;
    p->left = q;
    fixheight(q);
    fixheight(p);
    return p;
}

nodeavl* balance(nodeavl* p) // балансировка узла p
{
    fixheight(p);
    if (bfactor(p) == 2)
    {
        if (bfactor(p->right) < 0)
            p->right = rotateright(p->right);
        return rotateleft(p);
    }
    if (bfactor(p) == -2)
    {
        if (bfactor(p->left) > 0)
            p->left = rotateleft(p->left);
        return rotateright(p);
    }
    return p; // балансировка не нужна
}

nodeavl* insert(nodeavl* p, int k) // вставка ключа k в дерево с корнем p
{
    if (!p) return new nodeavl(k);
    if (k < p->key)
        p->left = insert(p->left, k);
    else
        p->right = insert(p->right, k);
    return balance(p);
}

nodeavl* findmin(nodeavl* p) // поиск узла с минимальным ключом в дереве p 
{
    return p->left ? findmin(p->left) : p;
}

nodeavl* removemin(nodeavl* p) // удаление узла с минимальным ключом из дерева p
{
    if (p->left == 0)
        return p->right;
    p->left = removemin(p->left);
    return balance(p);
}

nodeavl* remove(nodeavl* p, int k) // удаление ключа k из дерева p
{
    if (!p) return 0;
    if (k < p->key)
        p->left = remove(p->left, k);
    else if (k > p->key)
        p->right = remove(p->right, k);
    else //  k == p->key 
    {
        nodeavl* q = p->left;
        nodeavl* r = p->right;
        delete p;
        if (!r) return q;
        nodeavl* min = findmin(r);
        min->right = removemin(r);
        min->left = q;
        return balance(min);
    }
    return balance(p);
}

void treeprint(nodeavl* p) {
    if (p != NULL) { //Пока не встретится пустой узел
        cout << p->key << " "; //Отображаем корень дерева
        treeprint(p->left); //Рекурсивная функция для левого поддерева
        treeprint(p->right); //Рекурсивная функция для правого поддерева
    }
}

int HeightBTree(nodeavl* Tree)
{
    int x = 0, y = 0;
    if (Tree == NULL) return 0;     //пустое дерево или дошли до листа
    if (Tree->left) x = HeightBTree(Tree->left); //высота левого поддерева
    if (Tree->right) y = HeightBTree(Tree->right);  //высота правого поддерева
    if (x > y) return x + 1;    //+1 от корня к левому поддереву
    else return y + 1;   //+1 от корня к правому поддереву
}

unsigned int testbst(int array[])
{
    unsigned int start_time = clock();
    struct BSTnode* root = NULL;
    for (int i = 0; i < N; i++)
    {
        root = addnode(array[i], root);
    }
    unsigned int end_time = clock(); // конечное время
    unsigned int search_time = end_time - start_time;
    return search_time;
}

unsigned int testrbt(int array[])
{
    unsigned int start_time = clock();
    RBtree tree;
    for (int i = 0; i < N; i++)
    {
        tree.Insert(array[i]);
    }
    unsigned int end_time = clock(); // конечное время
    unsigned int search_time = end_time - start_time;
    return search_time;

}

unsigned int testavl(int array[])
{
    unsigned int start_time = clock();
    struct nodeavl* root = NULL;
    for (int i = 0; i < N; i++)
        root = insert(root, i);
    unsigned int end_time = clock(); // конечное время
    unsigned int search_time = end_time - start_time;
    return search_time;
}

int main()
{
    setlocale(LC_ALL, "Russian");
    int array[N];
    srand(time(0));
    unsigned int timeBST = 0;
    unsigned int timeRBT = 0;
    unsigned int timeAVL = 0;
    for (int i = 0; i < M; i++)
    {
        for (int i = 0; i < N; i++)
            array[i] = -50 + rand() % 100;
        timeBST += testbst(array);
        timeRBT += testrbt(array);
        timeAVL += testavl(array);
    }
    cout << timeBST / M << endl;
    cout << timeRBT / M << endl;
    cout << timeAVL / M << endl;
}
