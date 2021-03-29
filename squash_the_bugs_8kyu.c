#include <stddef.h>
#include <ctype.h>

size_t find_longest(const char *words) {
  size_t length = 0, max_length = 0;
  const char *pchar = words;
  
  char c;
  while ((c = *pchar++)) {
    if (isspace(c)) {
      if (length > max_length) {
        max_length = length;
      }
      length = 0;
    } else {
      length++;
    }
  }
  /* for the last word */
  if (length > max_length) {
      max_length = length;
  }
  return max_length;
}
