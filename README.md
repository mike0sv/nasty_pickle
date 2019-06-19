# nasty_pickle
Some nasty code to inject pickles with (almost) arbitrary code

### Usage

```
from nasty_pickle import patch_pickle_bytes

def my_bomb():
    print('kek')
    
pickle_payload = ...
payload_that_will_print_kek_on_unpickling = patch_pickle_bytes(pickle_payload, my_bomb)
```

`my_bomb` can contain any code that is convertible to oneliner, so no ifs, loops, exception handling and so on. 
And don't forget to include necessary imports