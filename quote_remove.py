#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014-2015 ourren
author: ourren <i@ourren.com>
"""
import StringIO

test = """Lee <ler762@gmail.com> wrote:

> On 1/25/15, Fabian Keil <fk@fabiankeil.de> wrote:

> > This does not affect the 3.0.23 source tarball because it's created and
> > signed
> > by me and Sourceforge currently doesn't let me to upload stuff to the
> > project
> > page.
>=20
> I uploaded it for you, but left the 3.0.23 folder marked as "hidden".
> Want it unhidden?

Yes, please.

Fabian
"""

def remove_quote(msg):
    """
    remove the previous email content.
    :param msg: email content
    :return: the clear content
    """
    ret_str = []
    buf = StringIO.StringIO(msg)
    for ii in buf.readlines():
        ii = ii.strip()
        if ii and not ii.startswith(">") and not ii.endswith("wrote:"):
            ret_str.append(ii)
    print " ".join(ret_str)

if __name__ == "__main__":
    print '+ begin remove quote +'
    remove_quote(test)