#install flask using python
package {'Flask':
  ensure   => '2.1.0',
  provider =>'pip3',
}
