#!/usr/bin/env python
import os
from newsetup.app import get_user_wanted_apps

if __name__ == "__main__":
    l = get_user_wanted_apps()
    print(l)
