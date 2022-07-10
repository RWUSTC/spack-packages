# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Pfd(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/singular-gpispace/PFD"
    url      = "https://github.com/singular-gpispace/PFD/archive/refs/tags/v0.02.tar.gz"
    git      = "git@github.com:singular-gpispace/PFD2"

    maintainers = ['MHeymann', 'jankoboehm', 'lristau', 'mrahn']

    version('latest', branch='public_candidate')

    depends_on('singular@snapshot_22_03')
    depends_on('gpi-space@22.03 ^libssh2@1.9')
    depends_on('flint@2.6.3')

    def cmake_args(self):
        spec = self.spec
        print(self.spec)
        args = [ self.define("GSPC_HOME", spec['gpi-space'].prefix)
               , self.define("SINGULAR_HOME", spec['singular'].prefix)
               , self.define("FLINT_HOME", spec['flint'].prefix)
               ]
        return args

    def setup_run_environment(self, env):
        spec = self.spec
        env.set('SINGULAR_INSTALL_DIR', spec['singular'].prefix)
        env.set('PFD_INSTALL_DIR', self.prefix)

