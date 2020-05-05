#include <Python.h>
/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: The Python object
 */
void print_python_list_info(PyObject *p)
{
	int Pysize = Py_SIZE(p);
	int ct;

	printf("[*] Size of the Python List = %d\n", Pysize);
	printf("[*] Allocated = %li\n", ((PyListObject *) p)->allocated);
	for (ct = 0; ct < Pysize; ct++)
		printf("Element %d: %s\n", ct,Py_TYPE(PyList_GetItem(p, ct))->tp_name);
}
