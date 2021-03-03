#!/usr/bin/env python
##ImmunityHeader v1
###############################################################################
## File       :  test_ccache.py
## Description:
##            :
## Created_On :  Mon Dec  8 22:49:19 PST 2014
## Created_By :  X.
##
## (c) Copyright 2010, Immunity, Inc. all rights reserved.
###############################################################################

## Script demonstrating the ability to read/write ccache files on Linux/Unix systems

'''
$ klist -f /tmp/krb5cc_1000
Ticket cache: FILE:/tmp/krb5cc_1000
Default principal: administrator@IMMU8.COM

Valid starting       Expires              Service principal
03/01/2017 14:27:17  04/01/2017 00:27:17  krbtgt/IMMU8.COM@IMMU8.COM
	renew until 04/01/2017 14:27:13, Flags: RIA
03/01/2017 14:43:34  04/01/2017 00:27:17  cifs/dc1@IMMU8.COM
	Flags: AO
$
'''

import sys
import logging

if "." not in sys.path:
    sys.path.append(".")

from ccache import CCache

# Test #1 is after kinit
s1  = '0504000c000100080000000000000000000000010000000100000009494d4d55382e43'
s1 += '4f4d0000000d61646d696e6973747261746f72000000010000000100000009494d4d55'
s1 += '382e434f4d0000000d61646d696e6973747261746f7200000002000000020000000949'
s1 += '4d4d55382e434f4d000000066b726274677400000009494d4d55382e434f4d00120000'
s1 += '0020ee2e7236da5b6e6927fca2068caa3795e53e4a85065a00923bb35f1da457a50058'
s1 += '6ba6b5586ba6b5586c3355586cf8310000e00000000000000000000000000427618204'
s1 += '233082041fa003020105a10b1b09494d4d55382e434f4da21e301ca003020102a11530'
s1 += '131b066b72627467741b09494d4d55382e434f4da38203e9308203e5a003020112a103'
s1 += '020104a28203d7048203d3b9d70197feee438d56c57ed7d1efc7e654a88bda5ae7f828'
s1 += '224bba3b6aae78b607586b79692a09f5be88c11446ea078251f6c9f909636418e2fea0'
s1 += '5b0d962fa6b4d909e50b7be86f9cc590753e364ec174786277f66201208c8c62cf0b81'
s1 += 'a590b98d1764b0df3cb848da07f478ae98a0d101a17f307e3f7c3dca4012dba21cdc42'
s1 += '89d5c366ba00e046802514d1b4006a699e4591c91121efffeedd1d7fb10cd45e53f26c'
s1 += '1aa5b59f36ac747279aaeecff0380e97b4a8087bfc3d09254e1518cceadb9a10c77ff0'
s1 += 'a2e5baff7ab85b3a8a4698de9e6ad83a67139deb542e88a3898ca721c1895c2281e59c'
s1 += 'f05ba26156d83dc36be295fd6a251da9aad980d7e2c2694fd416acfada0b2d59096130'
s1 += 'a2d62edf70d6890d2fcc2c2ced64d6e57c980eceb3bc755ad28065bc038f8ee277613f'
s1 += 'edb1d32dc2d3f210421796276243f28c5530bf988e775fa430d74780ac558361cdb8e2'
s1 += '683ed704563af0f0b2fb65f2d080ba0c8fc501061552bab8f4110d819c87f84e7f6dcc'
s1 += '471a816258bd88d8d77418b82ad6a56e3cda0f51627196571eea8570a1523617be353a'
s1 += '4a06e3126b16b11736c79f3f08f9cd54822bdc029e8159979d2f1a439d40ddd5aa270b'
s1 += '331d29000ff1ec1d0f043427bfe45f49b68f7eeefb128364ca37b15b48e6ecef7930b3'
s1 += '9eed2db183d6fce3779209a1f9ccd66db27153b7b033790429871f345b906ed3aac4ea'
s1 += '26373e7f1effbc75ea8d73b0fc4fa3662624e10b1c4ef1452180b1f157a88f6e6c0453'
s1 += '37b169e90ff9567fe699602eb45fa9c7ecdd785b0d91b9f23dd73ce45f0f3629d99a31'
s1 += '90e8963fea4fdb8bb768ca4667e987a311f25836da0426a1fd662526537e74691da808'
s1 += 'cbef3637fbc01fd79fce9ce7a3087a45c4aacd704a217f5c2bfeff9074142d6685ae05'
s1 += '7f250421bd5484abeee078b7b40f98eab88c4b2effc1257ebe220544f15ed732860c7c'
s1 += 'd05e22c9320777fc3cf51889cc39eeeb09b73ec52a32648fd4e278ba8cc9caac949eec'
s1 += 'c7dd3721f5b1d3cf232b10094b329bc7a0540fca34697a77ac80cfdbd34e165b35dd73'
s1 += '908b0149b5a429b97f4f4e251f751b85b8658f2bdaecc09dcebf85ce4b2cafe8a6508a'
s1 += '82a238036e16eb58537495cb99206f2d46428f4ccf26de25a344f893d4417f0aec2c6f'
s1 += 'afb04a0fdd094a60d3cef0aea96b40830a33c11cad72db11f6729d98aef78949564bf6'
s1 += 'c1118500a495482d13f73870b9d2b604ae1b67593d48a1172b0fe2901952b0c0fe6689'
s1 += '414bb198b649881eafab325ecddd08afb65518755b919fc6def01f589290c22a718898'
s1 += 'f78ead58f0153610cb0309084f6753e7fe1b41158e9bd4fa1d3a2b0fa486416dab1e69'
s1 += 'b95632ccd3fe0813b3ca00000000000000010000000100000009494d4d55382e434f4d'
s1 += '0000000d61646d696e6973747261746f7200000000000000030000000c582d43414348'
s1 += '45434f4e463a000000156b7262355f6363616368655f636f6e665f6461746100000007'
s1 += '70615f747970650000001a6b72627467742f494d4d55382e434f4d40494d4d55382e43'
s1 += '4f4d000000000000000000000000000000000000000000000000000000000000000000'
s1 += '0000000000013200000000'

# Test #2 is after smbclient -k
s2  = '0504000c000100080000000000000000000000010000000100000009494d4d55382e43'
s2 += '4f4d0000000d61646d696e6973747261746f72000000010000000100000009494d4d55'
s2 += '382e434f4d0000000d61646d696e6973747261746f7200000002000000020000000949'
s2 += '4d4d55382e434f4d000000066b726274677400000009494d4d55382e434f4d00120000'
s2 += '0020ee2e7236da5b6e6927fca2068caa3795e53e4a85065a00923bb35f1da457a50058'
s2 += '6ba6b5586ba6b5586c3355586cf8310000e00000000000000000000000000427618204'
s2 += '233082041fa003020105a10b1b09494d4d55382e434f4da21e301ca003020102a11530'
s2 += '131b066b72627467741b09494d4d55382e434f4da38203e9308203e5a003020112a103'
s2 += '020104a28203d7048203d3b9d70197feee438d56c57ed7d1efc7e654a88bda5ae7f828'
s2 += '224bba3b6aae78b607586b79692a09f5be88c11446ea078251f6c9f909636418e2fea0'
s2 += '5b0d962fa6b4d909e50b7be86f9cc590753e364ec174786277f66201208c8c62cf0b81'
s2 += 'a590b98d1764b0df3cb848da07f478ae98a0d101a17f307e3f7c3dca4012dba21cdc42'
s2 += '89d5c366ba00e046802514d1b4006a699e4591c91121efffeedd1d7fb10cd45e53f26c'
s2 += '1aa5b59f36ac747279aaeecff0380e97b4a8087bfc3d09254e1518cceadb9a10c77ff0'
s2 += 'a2e5baff7ab85b3a8a4698de9e6ad83a67139deb542e88a3898ca721c1895c2281e59c'
s2 += 'f05ba26156d83dc36be295fd6a251da9aad980d7e2c2694fd416acfada0b2d59096130'
s2 += 'a2d62edf70d6890d2fcc2c2ced64d6e57c980eceb3bc755ad28065bc038f8ee277613f'
s2 += 'edb1d32dc2d3f210421796276243f28c5530bf988e775fa430d74780ac558361cdb8e2'
s2 += '683ed704563af0f0b2fb65f2d080ba0c8fc501061552bab8f4110d819c87f84e7f6dcc'
s2 += '471a816258bd88d8d77418b82ad6a56e3cda0f51627196571eea8570a1523617be353a'
s2 += '4a06e3126b16b11736c79f3f08f9cd54822bdc029e8159979d2f1a439d40ddd5aa270b'
s2 += '331d29000ff1ec1d0f043427bfe45f49b68f7eeefb128364ca37b15b48e6ecef7930b3'
s2 += '9eed2db183d6fce3779209a1f9ccd66db27153b7b033790429871f345b906ed3aac4ea'
s2 += '26373e7f1effbc75ea8d73b0fc4fa3662624e10b1c4ef1452180b1f157a88f6e6c0453'
s2 += '37b169e90ff9567fe699602eb45fa9c7ecdd785b0d91b9f23dd73ce45f0f3629d99a31'
s2 += '90e8963fea4fdb8bb768ca4667e987a311f25836da0426a1fd662526537e74691da808'
s2 += 'cbef3637fbc01fd79fce9ce7a3087a45c4aacd704a217f5c2bfeff9074142d6685ae05'
s2 += '7f250421bd5484abeee078b7b40f98eab88c4b2effc1257ebe220544f15ed732860c7c'
s2 += 'd05e22c9320777fc3cf51889cc39eeeb09b73ec52a32648fd4e278ba8cc9caac949eec'
s2 += 'c7dd3721f5b1d3cf232b10094b329bc7a0540fca34697a77ac80cfdbd34e165b35dd73'
s2 += '908b0149b5a429b97f4f4e251f751b85b8658f2bdaecc09dcebf85ce4b2cafe8a6508a'
s2 += '82a238036e16eb58537495cb99206f2d46428f4ccf26de25a344f893d4417f0aec2c6f'
s2 += 'afb04a0fdd094a60d3cef0aea96b40830a33c11cad72db11f6729d98aef78949564bf6'
s2 += 'c1118500a495482d13f73870b9d2b604ae1b67593d48a1172b0fe2901952b0c0fe6689'
s2 += '414bb198b649881eafab325ecddd08afb65518755b919fc6def01f589290c22a718898'
s2 += 'f78ead58f0153610cb0309084f6753e7fe1b41158e9bd4fa1d3a2b0fa486416dab1e69'
s2 += 'b95632ccd3fe0813b3ca00000000000000010000000100000009494d4d55382e434f4d'
s2 += '0000000d61646d696e6973747261746f7200000000000000030000000c582d43414348'
s2 += '45434f4e463a000000156b7262355f6363616368655f636f6e665f6461746100000007'
s2 += '70615f747970650000001a6b72627467742f494d4d55382e434f4d40494d4d55382e43'
s2 += '4f4d000000000000000000000000000000000000000000000000000000000000000000'
s2 += '0000000000013200000000000000010000000100000009494d4d55382e434f4d000000'
s2 += '0d61646d696e6973747261746f72000000010000000200000009494d4d55382e434f4d'
s2 += '0000000463696673000000036463310012000000205ad24d96c2b3a1bb541e6ad754cd'
s2 += '19b4530798598089e5cc4d3518035a47b72f586ba6b5586baa86586c33550000000000'
s2 += '00240000000000000000000000000434618204303082042ca003020105a10b1b09494d'
s2 += '4d55382e434f4da2163014a003020101a10d300b1b04636966731b03646331a38203fe'
s2 += '308203faa003020112a103020104a28203ec048203e884c172dd83aa308b0ef37ed31f'
s2 += 'd80e2488e0dacf33b81cb0dce411ab6ce7601113b5069456a5f6a81c7fd924c75b257d'
s2 += '2412bb0a15717d66b997a9973cf9e9f1dde320fdaacff7b349d9e8cc70865745091335'
s2 += '4c66dfc3cd16217b5fa3c884d6f11713f134909967879d839dc250b324ee9c8e00d591'
s2 += 'cc05d1e1ee3ddf84b29d732e0e8fcfca666d18ca3f644ba41a5d4085c4e5cb5331e8f3'
s2 += 'b55096f8199ccb2b0f11454933bd6d15999a0909b4b3253e95339d6dc3eb258e29f0eb'
s2 += '7c7520782df5b588c335a3a9d5ab42c3f00838cd571be03c8d987f39e5543f69786cdd'
s2 += '6c0464fc9714c5b97fff1082e03544b094badab9b41054ecd61467a63d80ccb201d3d0'
s2 += 'c448caded2490e163e1faacd000e0879dc443642627fc7133c67cf9e9b2fd66189dfc0'
s2 += 'a2b13406e921134e30d0c2e533416605bcc8ea6430ba58b846e43514c299f405417328'
s2 += '54bf3a939c347fe5c4f34dc3414b74ebea57ef66896187a80132e3c4a666b8622bd50b'
s2 += 'fb5ad33fe996e68028696ea1c58f3357231cb413f981e6bf217185f9dc88c5a04abc46'
s2 += 'ba442f0e1b63d4b44f28b5cedfb4d7c6eddad47d792649d449c0724f6cf70e3901e819'
s2 += '1c8c9911f61235c87119621f750222223cfbbb25100dd5af57483fb935dd9c409e9e26'
s2 += '274a0b28ca972772e50cca432023e432306bb095883e1593a52f024a5b4ffd55fe5750'
s2 += '01cffe0491be2a0cc1e62b63e51e18106090c97929fe3c903eaa28348dae801927567e'
s2 += '6d671ef00b11bd99f12194dec2d09fb5bc9125a5493762ad45e64607160beaf827200d'
s2 += '293ee3e385bd513067de9b34257ba2a724c8eafb0e7c7d7cc3fcb4ae38a8d234579a83'
s2 += '2b9322a5be8bce6e0158f9d77ad7b1df2466e356f575f0f8aabfc52d9037d1bbe74311'
s2 += 'd6694452b9e62e0a6743883065a225e36a227520f36dd373c9a36be11dbe98a44d987c'
s2 += 'ca1b1226201e6111a96f036729a79c16b2c0225d9f760b59134bc2d376e8532287906a'
s2 += 'baf415b802c959691f82ab86c68c911f207ec9b017e971d05a6023bf734e8a2ffed3ef'
s2 += '3dea189333fc12472ad40b76977fbe92ccdc1e31627a75aac86c2da46e64bbc599da22'
s2 += '0554d426f5f720c94a6c23f8db81d36e61b4c06277b4d57dd715c7db9eccf9b082e828'
s2 += '25c563b470383502f2cb16d07d7f19d731496b61491c22594e36711ff8f623be0f738e'
s2 += 'fe7caf2771526e7da4898c288ff504c5dc45ddb71490da767c13bf786ef00b9d182d9b'
s2 += '4c932aeb12c9ff3c6766b8e12246ff6da47ae9e5e537c98c177beae7ad4b9ed16d45a1'
s2 += 'ba8deecf8cbd85459115ede296a646948b9a4213be940812d943afdb2600af979fa7ec'
s2 += '8305f46658e4e807876c196555c1949a2999f9a93472eb7dce261017acd01cbd757dd1'
s2 += 'f3fb5d61b100c600000000'

###
# Main to test the class!
###

def test_ccache(b):
    try:
        cc1 = CCache()
        cc1.set_raw_data(b)
        s = cc1.pack()
    except Exception as e:
        logging.error("Parsing error")
        return False
    else:
        return str(s) == str(b)

def main():

    logging.basicConfig(level=logging.INFO)

    if not test_ccache(s1.decode('hex')):
        logging.error("CCache test#1 failed.")
        sys.exit(1)
    else:
        logging.info("Success #1")

    if not test_ccache(s2.decode('hex')):
        logging.error("CCache test#2 failed.")
        sys.exit(2)
    else:
        logging.info("Success #2")


if __name__ == "__main__":
    main()