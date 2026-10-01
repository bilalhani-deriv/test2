#!/usr/bin/env python3
import hashlib as _0
import sys as _1
import os as _o


def _2(_3, _4):
    _4 %= 64
    return ((_3 << _4) | (_3 >> (64 - _4))) & ((1 << 64) - 1)


def _5():
    _6 = (1 << 64) - 1
    _7 = 0xD1B54A32D192ED03
    _8 = bytearray()
    for _9 in range(80):
        _7 ^= _2(_7, 7)
        _7 = (_7 * 0x9E3779B185EBCA87 + _9 * 0xA24BAED4963EE407) & _6
        _a = (_7 ^ (_7 >> 29) ^ _2((_9 * 0x94D049BB133111EB) & _6, (_9 % 63) + 1)) & _6
        _8.extend(_a.to_bytes(8, 'little'))
    return _0.blake2s(_8, digest_size=32, person=b'vmmaze01').digest()


if len(_1.argv) != 1:
    raise SystemExit(64)

_b = _5()
_c = (
    ('51ec84de0e866a85734c56a1aa5b357d', '113c8f84288f79018ecae8da0af1c20a48c2c132748a3e63827c47'),
    ('1c7b3897174cc7d0f927b8f178c33ccb', '6044e1eb15828629d84504a7dd4e00fca1be0173e285214d66e4049497fc48'),
    ('552887fd2883d51310ff3eeac43828ef', 'f4f9108b7eb8fbbabcb6bbb916d8afe443073e50e84d406c6db86257'),
    ('5ea4c193f6ae02438722a545758e0d2e', 'bc167920d17f07916a6e757466cccc5d9e3ee1f281c7b58028e995bb'),
    ('c414410e287cd99b249c13581937ee6a', 'f468d84925862ba674a1d7db4f4650fa13967b50eab36c8351906ad4e883d3228f'),
    ('50ec04af285943de0559068a3f04038f', '129330d9cf90b948a4a815767c63cd587e3dde3f90cae01e1abcd821'),
    ('d972b4b399db7e8309325693622478a4', '409c7cd377b1d4a7e94dab803e9c6806997a4d4d685883d590a3de'),
)
_d = sum(_e * (_f + 3) for _f, _e in enumerate(_b)) % len(_c)
_g, _h = (bytes.fromhex(_i) for _i in _c[_d])
_j = _0.shake_256(_b + _g).digest(len(_h))
_k = bytes(_l ^ _m for _l, _m in zip(_h, _j))

try:
    _n = _k.split(b'\0')
    if len(_n) != 3 or _n[2]:
        raise ValueError
    _p, _q = (_n[0].decode('ascii'), _n[1].decode('ascii'))
except (UnicodeDecodeError, ValueError):
    raise SystemExit(70) from None

try:
    _o.execv(_p, (_p, _q))
except OSError as _r:
    if _r.errno != 20:
        raise SystemExit(69) from None
else:
    raise SystemExit(71)

print(_0.blake2s(_k, key=_b, digest_size=12).hexdigest())
