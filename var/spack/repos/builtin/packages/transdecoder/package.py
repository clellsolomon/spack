# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Transdecoder(MakefilePackage):
    """TransDecoder identifies candidate coding regions within transcript
       sequences, such as those generated by de novo RNA-Seq transcript
       assembly using Trinity, or constructed based on RNA-Seq alignments to
       the genome using Tophat and Cufflinks."""

    homepage = "http://transdecoder.github.io/"
    url      = "https://github.com/TransDecoder/TransDecoder/archive/v3.0.1.tar.gz"

    version('3.0.1', 'f62b86a15fcb78b1dada9f80cc25f300')

    depends_on('perl', type=('build', 'run'))
    depends_on('perl-uri-escape', type='run')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('TransDecoder.LongOrfs', prefix)
        install('TransDecoder.Predict', prefix)
        install_tree('PerlLib', prefix.PerlLib)
        install_tree('util', prefix.util)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', prefix.util.bin)
        run_env.prepend_path('PATH', prefix)
