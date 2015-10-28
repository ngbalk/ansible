job('struts-job') {
    scm {
        git('git://github.com/ngbalk/test-sonatype.git')
    }
    triggers {
        scm('*/15 * * * *')
    }
    steps {
        maven('clean package')
    }
  configure{ project ->
    def scanStep = {
      project / 'postbuilders' /
    }
  }
}