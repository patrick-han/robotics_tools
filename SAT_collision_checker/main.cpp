#include <iostream>
#include <vector>

typedef struct Vertex2D
{
    float x;
    float y;
} Vertex2D;


class Polygon2D
{
    private:
        std::vector <Vertex2D> vertices;
        int num_vertices;
    public:
        Polygon2D();
        ~Polygon2D();

        void addVertex(Vertex2D& vx);

        int getNumVertices(void);
        void printVertices(void);
        
};

// Constructor
Polygon2D::Polygon2D(void)
{
    num_vertices = 0;
}

// Destructor
Polygon2D::~Polygon2D(void)
{
}

// Add a vertex, increment the number of vertices
void Polygon2D::addVertex(Vertex2D& vx)
{
    vertices.push_back(vx);
    num_vertices++;
}

// Return the number of vertices
int Polygon2D::getNumVertices(void)
{
    return num_vertices;
}

// Print out all the vertices
void Polygon2D::printVertices(void)
{
    for (auto v: vertices)
    {
        std::cout << "{" << v.x << " " << v.y << "}" << std::endl;
    }
}


// Inputs: Two Polygon2D objects
// Output: Whether or not they are colliding
int SAT_CollisionChecker(Polygon2D& p1, Polygon2D& p2)
{
    return 0;
}


// Driver code
int main ()
{
    // Define geometry of the square
    Vertex2D s1{0, 6};
    Vertex2D s2{0, 0};
    Vertex2D s3{6, 0};
    Vertex2D s4{6, 6};

    Polygon2D square;
    square.addVertex(s1);
    square.addVertex(s2);
    square.addVertex(s3);
    square.addVertex(s4);
    square.printVertices();
    std::cout << square.getNumVertices() << std::endl;

    // Define geometry of the triangle
    Vertex2D t1{3, 3};
    Vertex2D t2{15, 3};
    Vertex2D t3{4, 10};

    Polygon2D triangle;
    triangle.addVertex(t1);
    triangle.addVertex(t2);
    triangle.addVertex(t3);
    triangle.printVertices();
    std::cout << triangle.getNumVertices() << std::endl;

    std::cout << (SAT_CollisionChecker(square, triangle) ? "Colliding" : "Not Colliding") << std::endl;
}