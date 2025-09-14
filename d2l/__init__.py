# d2l/__init__.py — a lightweight aggregator (no external deps bundled)

# stdlib
import collections as collections
import hashlib as hashlib
import inspect as inspect
import math as math
import os as os
import random as random
import re as re
import shutil as shutil
import sys as sys
import tarfile as tarfile
import time as time
import zipfile as zipfile
from collections import defaultdict as defaultdict

# third-party: import gently so the package still imports even if some are missing
def _optional_import(name, attr=None):
    try:
        mod = __import__(name, fromlist=['*'])
        return getattr(mod, attr) if attr else mod
    except Exception as e:
        class _Missing:
            def __getattr__(self, _):
                raise ImportError(f"Optional dependency '{name}' not available: {e}")
        return _Missing()

pd = _optional_import('pandas')
requests = _optional_import('requests')
display = _optional_import('IPython.display')
plt = _optional_import('matplotlib.pyplot')
backend_inline = _optional_import('matplotlib_inline.backend_inline')

np = _optional_import('numpy')
torch = _optional_import('torch')
nn = _optional_import('torch', 'nn')
F = _optional_import('torch.nn.functional')
torchvision = _optional_import('torchvision')
transforms = _optional_import('torchvision.transforms')
Image = _optional_import('PIL.Image')
distance_matrix = _optional_import('scipy.spatial', 'distance_matrix')

# small quality-of-life helpers so it feels a bit like the real d2l
def use_svg_display():
    """Prefer SVG for crisper plots in notebooks (if inline backend available)."""
    if hasattr(backend_inline, 'set_matplotlib_formats'):
        backend_inline.set_matplotlib_formats('svg')

def set_figsize(size=(3.5, 2.5)):
    """Set default figure size."""
    if hasattr(plt, 'rcParams'):
        plt.rcParams['figure.figsize'] = size

def plot(x, ys, xlabel=None, ylabel=None, legend=None, figsize=(3.5, 2.5)):
    """Quick plot helper, mimicking d2l.plot."""
    set_figsize(figsize)
    if not hasattr(ys[0], "__len__"):  # single curve
        ys = [ys]
    for y in ys:
        plt.plot(x, y)
    if legend:
        plt.legend(legend)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)

__all__ = [
    # stdlib
    'collections','hashlib','inspect','math','os','random','re','shutil','sys',
    'tarfile','time','zipfile','defaultdict',
    # third-party
    'pd','requests','display','plt','backend_inline','np','torch','torchvision',
    'Image','distance_matrix','nn','F','transforms',
    # helpers
    'use_svg_display','set_figsize','plot',
]
