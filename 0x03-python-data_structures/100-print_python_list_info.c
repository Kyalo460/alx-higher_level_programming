#include <stdio.h>
#include "Python.h"

/**
  *print_python_list_info - prints list info from python script
  *@p: pointer to the list
  */

void print_python_list_info(PyObject *p)
{
	PyListObject *pp = (PyListObject *)p;
	int i;

	printf("[*] Size of the Python List = %lu\n", pp->ob_base.ob_size);
	printf("[*] Allocated = %lu\n", pp->allocated);

	for (i = 0; i < pp->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", i, pp->ob_item[i]->ob_type->tp_name);
	}
}
