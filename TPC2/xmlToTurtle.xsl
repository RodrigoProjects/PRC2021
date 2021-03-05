<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xd="oxygenxml.com/ns/doc/xsl"
    exclude-result-prefixes="xd"
    version="1.0">
    
    <xd:doc scope="stylesheet">
        
        <xd:desc>
            
            <xd:p><xd:b>Created on:</xd:b> Mar 4, 2021</xd:p>
            
            <xd:p><xd:b>Author:</xd:b> Rodrigo Pimentel</xd:p>
            
            <xd:p>Conversão do arquivo musical em XML para TTL</xd:p>
            
        </xd:desc>
        
    </xd:doc>
    
    
    
    <xsl:output method="text" encoding="UTF-8" indent="yes"/>
       
     <xsl:template match="obra">
        
        <xsl:for-each select="instrumentos/instrumento">
            ###  http://www.semanticweb.org/rodrigo/ontologies/prc2021/arquivo-musical#partitura_<xsl:value-of select="generate-id(partitura)" />
            :partitura_<xsl:value-of select="generate-id(partitura)"/> rdf:type owl:NamedIndividual ,
            :Partitura ;
            :path "<xsl:value-of select="partitura/@path"/>" ;
            :tipo "<xsl:value-of select="partitura/@type"/>" ;
            :voz <xsl:choose>
                <xsl:when test="partitura/@voz">"<xsl:value-of select="partitura/@voz"/>" .
                </xsl:when>
                <xsl:otherwise>"None" .
                </xsl:otherwise>
                
            </xsl:choose> 
            
            ###  http://www.semanticweb.org/rodrigo/ontologies/prc2021/arquivo-musical#instrumento_<xsl:value-of select="generate-id()" />
            :instrumento-<xsl:value-of select="generate-id()" /> rdf:type owl:NamedIndividual ,
            :Instrumento ;
            :temPartitura :partitura_<xsl:value-of select="generate-id(partitura)" /> ;
            :designação "<xsl:value-of select="designacao" />" .
            
        </xsl:for-each>
            
            <xsl:if test="compositor">
            ###  http://www.semanticweb.org/rodrigo/ontologies/prc2021/arquivo-musical#compositor_<xsl:value-of select="generate-id(compositor)"/> ;
            :compositor_<xsl:value-of select="generate-id(compositor)"/> rdf:type owl:NamedIndividual ,
            :Compositor ;
            :nome "<xsl:value-of select="compositor"/>" .                    
            </xsl:if>
            
            
            ###  http://www.semanticweb.org/rodrigo/ontologies/prc2021/arquivo-musical#obra_<xsl:value-of select="@id" />
            :obra_<xsl:value-of select="@id" /> rdf:type owl:NamedIndividual ,
            :Obra ;
            <xsl:for-each select="instrumentos/instrumento">:temInstrumento :instrumento_<xsl:value-of select="generate-id()" /> ;
            </xsl:for-each>:tipo "<xsl:value-of select="tipo" />" ;
            <xsl:if test="compositor">:temCompositor :compositor_<xsl:value-of select="generate-id(compositor)"/> ;</xsl:if>
            :titulo "<xsl:value-of select="titulo" />" .

     </xsl:template>
     
</xsl:stylesheet>