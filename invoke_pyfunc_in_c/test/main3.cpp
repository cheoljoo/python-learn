#include <Python.h>

void myClass() {
    PyObject* mydef = PyImport_ImportModule("scripts.my_def");
    int result;

    if (mydef) {
        PyObject* myClass = PyObject_GetAttrString(mydef, "MyClass");

        if (myClass) {
            /* instance = MyClass() */
            PyObject *instance = PyObject_CallObject(myClass, NULL);

            if (instance) {
                PyObject *returnSum = PyObject_CallMethod(instance, "Sum",
                        NULL);
                if (returnSum) {
                    double result = PyFloat_AS_DOUBLE(returnSum); //find using Search . Type this "PyFloat_"
                    Py_XDECREF (returnSum);
                    printf("sum = %f\n", result);
                }else printf("No Sum Method\n");

                PyObject *returnAvr = PyObject_CallMethod(instance, "Avr","i", 4);
                if (returnAvr) {
                    double result = PyFloat_AS_DOUBLE(returnAvr); //find using Search . Type this "PyFloat_"
                    Py_XDECREF (returnAvr);
                    printf("Avr = %f\n", result);
                }else printf("No Avr Method\n");
            }
        }
    }
}

int main(int argc, char** argv) {
    Py_SetProgramName(argv[0]);
    Py_Initialize();
    printf("GetProgramName: %s\n\n", Py_GetProgramName());

    if (Py_IsInitialized()) {
        PySys_SetArgv(argc, argv);
        printf("GetPath: %s\n\n", Py_GetPath());
        myClass();
        Py_Finalize();
    }
    return 0;
}
