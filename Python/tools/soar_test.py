#!/usr/bin/env python2.7

import Python_sml_ClientInterface as sml

k = sml.Kernel.CreateKernelInNewThread()
a = k.CreateAgent('soar')
print(a.ExecuteCommandLine('echo hello world'))
